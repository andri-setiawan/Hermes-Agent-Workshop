# Stitch with Google & UI Prototyping

## Get Stitch API Key
1. Visit https://stitch.withgoogle.com/
2. Create app / get API key
3. Add to `.env`:
   ```
   STITCH_API_KEY=your_key_here
   ```

## Usage
Use Stitch + Hermes browser tools to:
- Build UI app prototypes visually
- Generate frontend from natural language
- Export to HTML/React

## Quick Test
```bash
curl -s -H "Authorization: Bearer $STITCH_API_KEY" https://stitch.withgoogle.com/api/v1/...
```
