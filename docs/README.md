# GitHub Pages site (Jekyll)

This folder is the **Jekyll source** for the catalog’s public site. The main page body is generated from the repository root `README.md` so the list stays single-sourced.

## One-time repository settings

1. **Settings → Pages → Build and deployment**
   - **Source:** GitHub Actions (not “Deploy from a branch”).
2. After the first successful run of [`.github/workflows/pages.yml`](../.github/workflows/pages.yml), open the live URL (default: `https://haoruilee.github.io/awesome-agent-native-services/`).
3. **Settings → General → Social preview** — set the image to `docs/assets/images/social-preview.png` for richer cards on social platforms.

## Local regeneration (optional)

From the repo root:

```bash
bash scripts/build-github-pages.sh
```

Then build with Jekyll using the same stack as GitHub (`bundle install` in `docs/`, then `bundle exec jekyll build`), or rely on CI.
