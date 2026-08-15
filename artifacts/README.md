# Result artifacts

`freeze_packet_v2.tar.gz` is the immutable final result packet. Its SHA-256 is:

```text
a009d5678d46927b63d6cda9207a73af8a6b886485df9e747ac986cedf7307ab
```

`freeze_packet_v2/` is a public reporting subset containing the endpoint specification, claim ledger, manifest, and compact derived tables. The full archive was expanded during verification: `MANIFEST.json` tracks 35 payload files and all 35 hashes matched, and `claims.py` resolved 21/21 claims with no missing files or errors. Harness source and raw/private episode exports remain inside the immutable archive rather than the extracted repository tree, consistent with the repository boundary.

The packet's embedded `README.md` retains an older v1 heading for provenance; use `ENDPOINTS.md`, `claims.json`, and the manifest changelog as the v2 canonical reporting specification.
