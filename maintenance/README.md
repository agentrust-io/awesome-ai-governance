# Listing metadata prototype

This is a reviewable first slice of issue #167, not an adopted listing policy.
It proposes an optional companion JSON file while keeping the human-readable
README authoritative. No existing listing has been migrated, reverified or
removed. Maintainers still need to choose the storage format and initial real
sample. No CI gate is added by this prototype.

## Run offline

Python 3.11 or later, standard library only:

```sh
python -m unittest discover -s tests -v
python tools/check_listing_metadata.py maintenance/synthetic-example.json --as-of 2026-10-21
```

The supplied example is fictional and uses reserved example.org URLs. Its dates
and reviewer are test data, not attestations about any listed project.

The document has exactly `schema_version` (integer 1) and `entries` (array).
Every entry has these nonempty, trimmed string fields:

| Field | Meaning |
| --- | --- |
| `name` | Listing name |
| `url` | Canonical listing URL selected by a human |
| `category` | Category selected by a human |
| `description` | Short neutral description |
| `availability` | `open-source`, `free-tier`, or `published-specification` |
| `availability_evidence` | URL supporting that availability basis, such as license/specification/free-tier terms |
| `commercial_disclosure` | Explicit disclosure, including when no commercial offering is known |
| `last_verified` | Human verification date, YYYY-MM-DD |
| `reviewer` | Person or review identity responsible for the record |
| `verification_evidence` | Review or source URL recording the verification basis |

The validator checks shape, duplicate JSON keys, required fields, availability
vocabulary, URL syntax within this prototype's restricted profile, duplicate
canonical URLs and real calendar dates no later than the explicit `--as-of`
cutoff. A fixed cutoff makes repeated runs deterministic. It is caller input,
not proof of when a review occurred. Empty arrays are allowed for an incremental
migration; the success message reports the count.

URL fields use HTTPS with a DNS hostname, no credentials, no whitespace or
backslashes, and no nondefault port. For duplicate detection only, host case and
port 443 are normalized, fragments are ignored, and an empty path becomes `/`.
Path case, trailing slashes on nonempty paths and query strings are preserved.
Redirect aliases and equivalent percent encodings are not detected. This is a
conservative comparison rule, not a universal URL canonicalization algorithm.
Resources that require another URL form need a reviewed format change rather
than fabricated HTTPS addresses.

## Human review and remaining work

A successful run establishes metadata structure only. It does not establish
link reachability, maintenance status, license validity, commercial eligibility,
reviewer authenticity, truthful descriptions, neutral wording, category
membership, or correspondence with the current README. Verify those separately
against primary sources before adding real metadata. Do not advance a review
date merely because this script passes. Record any editorial exception and its
rationale in the contribution review; do not weaken validation silently.

The repository already has a separate Lychee network-link workflow. This script
makes no network requests and does not alter that workflow. Future adoption
should decide how to reconcile metadata with README listings and how to handle
transient network errors without automatically deleting entries. No automatic
approval, ranking, universal recent-commit cutoff or stale-list removal is
implemented here.
