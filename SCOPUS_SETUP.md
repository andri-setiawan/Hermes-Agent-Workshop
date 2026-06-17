# Scopus API for SLR Research

## 1. Get API Key
- Register: https://dev.elsevier.com/
- Create API Key (free tier: ~20k requests/week)
- Add to `~/.hermes/.env`:
  ```
  SCOPUS_API_KEY=dfab6607561f0ec284cb773723395644
  ```

## 2. Use with Hermes

Hermes has the Scopus skill loaded. Query example:

```
"Search Scopus for federated learning in healthcare papers, show DOI and citation counts"
```

## 3. Manual Search
```bash
curl -s "https://api.elsevier.com/content/search/scopus?query=TITLE-ABS-KEY(machine+learning+healthcare)&count=10" \
  -H "X-ELS-APIKey: $SCOPUS_API_KEY" \
  -H "Accept: application/json"
```
