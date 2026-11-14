import copy
from datetime import date
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from check_listing_metadata import canonical_url, unique_object, validate


class MetadataTests(unittest.TestCase):
    def setUp(self):
        self.record = {
            'name': 'Synthetic tool', 'url': 'https://example.org/tool',
            'category': 'Synthetic category', 'description': 'Synthetic test record.',
            'availability': 'open-source',
            'availability_evidence': 'https://example.org/tool/license',
            'commercial_disclosure': 'Synthetic disclosure; not a real listing.',
            'last_verified': '2026-10-21', 'reviewer': 'synthetic-reviewer',
            'verification_evidence': 'https://example.org/review/1',
        }
        self.document = {'schema_version': 1, 'entries': [self.record]}
        self.cutoff = date(2026, 10, 21)

    def test_valid_availability_bases(self):
        for basis in ('open-source', 'free-tier', 'published-specification'):
            self.record['availability'] = basis
            self.assertEqual(validate(self.document, self.cutoff), [])

    def test_missing_unknown_empty_and_wrong_type_fields(self):
        for field in self.record:
            for bad in ('missing', '', None, [], '  padded  '):
                with self.subTest(field=field, bad=bad):
                    doc = copy.deepcopy(self.document)
                    if bad == 'missing':
                        del doc['entries'][0][field]
                    else:
                        doc['entries'][0][field] = bad
                    self.assertTrue(validate(doc, self.cutoff))
        self.record['unrecognized'] = 'value'
        self.assertTrue(validate(self.document, self.cutoff))

    def test_duplicate_urls_are_refused(self):
        self.record['url'] = 'https://EXAMPLE.org:443#one'
        duplicate = copy.deepcopy(self.record)
        duplicate['url'] = 'https://example.org/#two'
        self.document['entries'].append(duplicate)
        self.assertIn('duplicates entries[0]', '\n'.join(validate(self.document, self.cutoff)))

    def test_distinct_paths_queries_and_trailing_slashes_remain_distinct(self):
        urls = ['https://example.org/A', 'https://example.org/a',
                'https://example.org/a/', 'https://example.org/a?version=1',
                'https://example.org/a?version=2']
        self.assertEqual(len({canonical_url(url) for url in urls}), len(urls))

    def test_invalid_urls(self):
        for url in ('http://example.org', '/relative', 'javascript:alert(1)',
                    'https://user:pass@example.org', 'https://example.org:444',
                    'https://example.org:abc', 'https://[bad', 'https://localhost',
                    'https://example.org/with space', 'https://example.org/\npath',
                    'https://example.org\\other'):
            with self.subTest(url=url):
                with self.assertRaises(ValueError):
                    canonical_url(url)

    def test_invalid_and_future_dates(self):
        for value in ('2026-02-30', '20261021', '2026-1-1', '2026-10-22'):
            self.record['last_verified'] = value
            self.assertTrue(validate(self.document, self.cutoff))

    def test_wrong_document_shapes_and_availability(self):
        for doc in (None, [], {}, {'schema_version': True, 'entries': []},
                    {'schema_version': 2, 'entries': []},
                    {'schema_version': 1, 'entries': {}},
                    {'schema_version': 1, 'entries': [None]}):
            self.assertTrue(validate(doc, self.cutoff))
        self.record['availability'] = 'commercial-only'
        self.assertTrue(validate(self.document, self.cutoff))

    def test_duplicate_json_keys(self):
        with self.assertRaises(ValueError):
            json.loads('{"schema_version":1,"schema_version":2}', object_pairs_hook=unique_object)

    def test_cli_exit_codes_and_no_approval_claim(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'metadata.json'
            command = [sys.executable, str(ROOT / 'tools/check_listing_metadata.py'),
                       str(path), '--as-of', '2026-10-21']
            path.write_text(json.dumps(self.document))
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('not editorial approval', result.stdout)
            for content in ('{', '{"schema_version":1,"schema_version":2}',
                            json.dumps({'schema_version': 1, 'entries': [self.record, self.record]})):
                path.write_text(content)
                result = subprocess.run(command, capture_output=True, text=True)
                self.assertEqual(result.returncode, 1)
                self.assertNotIn('Traceback', result.stderr)
            path.unlink()
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)


if __name__ == '__main__':
    unittest.main()
