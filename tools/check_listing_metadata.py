"""Offline validation of the proposed listing metadata format (issue #167)."""

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit, urlunsplit

FIELDS = {
    'name', 'url', 'category', 'description', 'availability',
    'availability_evidence', 'commercial_disclosure', 'last_verified',
    'reviewer', 'verification_evidence',
}


def canonical_url(value):
    """Conservative duplicate key; never fetch URLs or follow redirects."""
    if not isinstance(value, str) or re.search(r'[\s\\\x00-\x1f\x7f]', value):
        raise ValueError('expected an absolute HTTPS URL without whitespace or backslashes')
    try:
        parts = urlsplit(value)
        host = parts.hostname
        port = parts.port
    except ValueError as exc:
        raise ValueError('invalid URL authority') from exc
    if (parts.scheme != 'https' or not host or parts.username is not None
            or parts.password is not None or port not in (None, 443)
            or not re.fullmatch(r'[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*', host)
            or '.' not in host):
        raise ValueError('expected an HTTPS DNS host without credentials or a nondefault port')
    return urlunsplit(('https', host.lower(), parts.path or '/', parts.query, ''))


def parse_date(value):
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        raise ValueError('expected YYYY-MM-DD')
    return date.fromisoformat(value)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON key: {key}')
        result[key] = value
    return result


def validate(document, as_of):
    errors = []
    if (not isinstance(document, dict) or set(document) != {'schema_version', 'entries'}
            or type(document['schema_version']) is not int or document['schema_version'] != 1
            or not isinstance(document['entries'], list)):
        return ['document: expected schema_version 1 and an entries array only']
    seen = {}
    for index, entry in enumerate(document['entries']):
        prefix = f'entries[{index}]'
        if not isinstance(entry, dict) or set(entry) != FIELDS:
            errors.append(f'{prefix}: expected exactly the documented fields')
            continue
        for field in sorted(FIELDS):
            value = entry[field]
            if not isinstance(value, str) or not value.strip() or value != value.strip():
                errors.append(f'{prefix}.{field}: expected a nonempty trimmed string')
        for field in ('url', 'availability_evidence', 'verification_evidence'):
            try:
                key = canonical_url(entry[field])
                if field == 'url':
                    if key in seen:
                        errors.append(f'{prefix}.url: duplicates entries[{seen[key]}]')
                    else:
                        seen[key] = index
            except ValueError as exc:
                errors.append(f'{prefix}.{field}: {exc}')
        if entry['availability'] not in ('open-source', 'free-tier', 'published-specification'):
            errors.append(f'{prefix}.availability: unsupported availability basis')
        try:
            verified = parse_date(entry['last_verified'])
            if verified > as_of:
                errors.append(f'{prefix}.last_verified: later than --as-of')
        except ValueError as exc:
            errors.append(f'{prefix}.last_verified: {exc}')
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('metadata', type=Path)
    parser.add_argument('--as-of', required=True, type=parse_date,
                        help='explicit review cutoff, YYYY-MM-DD; no wall-clock dependency')
    args = parser.parse_args(argv)
    try:
        document = json.loads(args.metadata.read_text(encoding='utf-8'),
                              object_pairs_hook=unique_object)
        errors = validate(document, args.as_of)
    except (OSError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(document['entries'])} metadata records; structure only, not editorial approval")
    return 0


if __name__ == '__main__':
    sys.exit(main())
