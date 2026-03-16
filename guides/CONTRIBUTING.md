# Contributing to Pack Dashboard

Welcome! We're building a data commons for people, not corporations. Your contributions help.

---

## Ways to Contribute

### 1. Code

- **Bug fixes**: Find issues labeled `bug`, submit a PR
- **Features**: Pick an issue labeled `enhancement` or open a new one
- **Bounties**: See issues labeled `bounty` for paid work ($25-$2000)

### 2. Documentation

- Improve guides (VECTOR_INDEX_GUIDE.md, SUPABASE_SETUP.md, etc.)
- Add tutorials or use-case examples
- Write translations (Spanish, French, Chinese, etc.)
- Clarify confusing sections

### 3. Community

- Answer questions in GitHub Discussions
- Report bugs (clear, reproducible steps help)
- Share how you use Pack Dashboard (testimonials, case studies)
- Join Advisory Board (if you represent a non-profit or grassroots org)

### 4. Advocacy

- Star ⭐ the repo (helps discoverability)
- Tell friends, colleagues, community members
- Present at meetups, conferences, universities
- Write blog posts about your experience

### 5. Design & UX

- Suggest UI improvements (open an issue with mockups)
- Accessibility audit (color contrast, keyboard nav, screen reader tests)
- Usability testing (can we make it easier to use?)

### 6. Security

- Responsible disclosure: security@awanet.nz (don't post vulns publicly)
- Code review for security issues
- Compliance review (GDPR, CCPA, etc.)

---

## Getting Started

### Prerequisites

- Node 18+ & npm
- Git
- Basic TypeScript knowledge (optional but helpful)

### 1. Fork & Clone

```bash
git clone https://github.com/yourusername/pack-dashboard.git
cd pack-dashboard
npm install
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
# or
git checkout -b docs/improve-docs
```

### 3. Make Your Changes

```bash
# Run dev server
npm run dev

# Run tests (if applicable)
npm run test

# Type check
npm run typecheck

# Lint & format
npm run lint
npm run format
```

### 4. Commit with Clear Messages

```bash
git add .
git commit -m "feat: add search filters to PacksTable

- Add filter UI controls (date, tags, similarity threshold)
- Persist filters in URL params
- Add unit tests (80%+ coverage)

Closes #123"
```

**Commit message format**: `[type]: [description]`

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`

### 5. Push & Open a Pull Request

```bash
git push origin feature/your-feature-name
```

**PR Title**: Same as commit message

**PR Description** (use template):

```markdown
## What?

Brief description of changes.

## Why?

Why is this change needed?

## How?

How does it work?

## Testing?

How did you test it? Steps to reproduce.

## Checklist

- [ ] TypeScript passes (`npm run typecheck`)
- [ ] No eslint errors (`npm run lint`)
- [ ] Tests added/updated (if applicable)
- [ ] Docs updated (if applicable)
- [ ] No secrets committed (no .env, keys, passwords)

## Screenshots (if UI change)

Before / After screenshots.
```

### 6. Respond to Feedback

Maintainers will review within 3-5 business days. Iterate based on feedback.

Once approved, we merge and celebrate! 🎉

---

## Code Quality

### TypeScript

- Strict mode enabled (`strict: true`)
- No `any` types (use `unknown` or specific types)
- Document complex types

Example:

```typescript
// ❌ Avoid
function search(query: any): any {
  return data.filter((x) => x.includes(query));
}

// ✅ Good
interface SearchResult {
  id: string;
  name: string;
  similarity: number;
}

function search(query: string): SearchResult[] {
  return data
    .filter((item) => item.name.includes(query))
    .map((item) => ({
      id: item.id,
      name: item.name,
      similarity: calculateSimilarity(query, item.name),
    }));
}
```

### Testing

- Aim for 80%+ coverage on new code
- Use Vitest for unit tests
- Test edge cases (empty input, null, invalid types)

Example:

```typescript
// src/lib/embedding.test.ts
import { generateEmbeddingFromText } from "./embedding";
import { expect, test } from "vitest";

test("generateEmbeddingFromText returns 384-dim vector", async () => {
  const embedding = await generateEmbeddingFromText("hello");
  expect(embedding).toHaveLength(384);
  expect(embedding.every((x) => x >= -1 && x <= 1)).toBe(true);
});

test("deterministic: same input produces same output", async () => {
  const emb1 = await generateEmbeddingFromText("test");
  const emb2 = await generateEmbeddingFromText("test");
  expect(emb1).toEqual(emb2);
});

test("empty string produces valid vector", async () => {
  const embedding = await generateEmbeddingFromText("");
  expect(embedding).toHaveLength(384);
});
```

### Formatting & Linting

```bash
# Auto-format
npm run format

# Check for issues
npm run lint
```

(ESLint + Prettier configured in `eslintrc.json` + `prettier.json`)

### Documentation

- Add JSDoc comments to exported functions
- Update README/docs if behavior changes
- Link issues in commit messages (`Closes #123`)

Example:

```typescript
/**
 * Generate deterministic vector from text using SHA-256 hashing
 *
 * @param text - Input text to embed
 * @returns Promise resolving to 384-dimensional normalized vector
 *
 * @example
 * const embedding = await generateEmbeddingFromText('hello')
 * // [0.5, -0.2, ..., 0.1] (384 values)
 */
export async function generateEmbeddingFromText(
  text: string
): Promise<number[]> {
  // ...
}
```

---

## Bounty Program

Want to get paid for contributions?

### How It Works

1. **Find a bounty**: Issues labeled `bounty` in GitHub
2. **Claim it**: Comment on the issue with your GitHub handle
3. **Code it**: 3-7 days typical turnaround
4. **Submit PR**: Link to the bounty issue
5. **Get paid**: $25-$2000 within 7 days of merge

### Bounty Eligibility

- Must sign **Contributor License Agreement (CLA)**
- Code must pass review (same quality as regular PRs)
- No plagiarism or ghost code (ChatGPT is fine as a tool, but code must be yours)

### Bounty Amounts

| Difficulty   | Time Est.   | Amount    |
| ------------ | ----------- | --------- |
| Beginner     | 1-2 hours   | $25-50    |
| Intermediate | 2-8 hours   | $50-200   |
| Advanced     | 8-40 hours  | $200-1000 |
| Research     | 20-80 hours | $500-2000 |

### Claiming a Bounty

```markdown
## Bounty Application

**GitHub**: @yourhandle
**Estimate**: 6 hours
**Experience**: [Brief relevant experience]
**Timeline**: [When you can start/finish]

I'd love to work on this. [Why you're a good fit]
```

Maintainers approve within 48 hours. Then you code!

### Getting Paid

Options: Stripe, PayPal, Crypto (BTC/ETH), or donate to charity.

Email bounty@awanet.nz with:

```
GitHub: @yourhandle
Issue: #123
Amount: $200
Payment: Stripe / PayPal / Crypto / Charity
Contact: [email or crypto address]
```

---

## Contributor License Agreement (CLA)

By submitting code, you agree to:

1. **Grant AwaNet copyright rights** to your contribution
2. **Your code will be licensed** under AGPL-3.0 (with commercial exception)
3. **AwaNet can dual-license** if needed (to relicense under different terms in future)
4. **You retain credit** (name in CONTRIBUTORS.md + commit history)

**Benefits to you**:

- Your code becomes part of a commons
- Others can build on it
- You're credited forever

**Why we need this**:

- Single license authority (avoids fragmentation)
- Flexibility to relicense (e.g., if AGPL becomes outdated)
- Protection against contributor harassment

**CLA Form** (submit with PR):

```markdown
I agree to contribute code to Pack Dashboard under the AGPL-3.0 license.

I grant AwaNet rights to use, modify, and relicense my contributions.

I confirm I wrote this code (or have permission to contribute it).

Signed: [Your Name]
Date: [Today]
GitHub: @yourhandle
```

---

## Code of Conduct

We're building for humans. Respect each other.

- **Be kind**: Disagreements are OK; personal attacks are not
- **Be inclusive**: Welcome all backgrounds, experience levels, identities
- **Be transparent**: Disclose conflicts of interest (working for company using this, etc.)
- **Be humble**: Learn from feedback, admit mistakes

**Violations?** Report to conduct@awanet.nz (confidential)

---

## Maintainers

Current maintainers:

- **@awanet-team**: Core development, releases, security

If you're interested in becoming a maintainer (reviewing PRs, triaging issues), let us know: maintainers@awanet.nz

---

## Release Process

We follow semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR**: Breaking changes (AGPL-3.0 license stays, no backward compat)
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

**Release schedule**: Roughly monthly, when meaningful changes accumulate.

**To check version**: See `package.json` + GitHub Releases

---

## FAQ

**Q: Can I contribute even though I work for a company?**

A: Yes! Just disclose in your PR (e.g., "Contributed as part of Acme Corp's open-source policy"). No conflicts of interest with AGPL model.

**Q: What if my company uses Pack Dashboard?**

A: Great! If they're <$1M revenue / <10 employees, they're free tier. Otherwise, they buy a license (good for both communities). See `FREE_TIER_ELIGIBILITY.md`.

**Q: Do I need to be a TypeScript expert?**

A: No! We value contributions in any area (docs, design, testing, community). TypeScript skills help but aren't required.

**Q: Can I contribute anonymously?**

A: Yes! Use a GitHub account without identifying info. We'll credit you as-is.

**Q: What if I disagree with project direction?**

A: Open an issue + let's discuss! We're community-oriented and open to feedback. Major decisions go to Advisory Board.

**Q: How long does code review take?**

A: 3-5 business days for feedback. Sometimes faster. We balance thoroughness + responsiveness.

**Q: Can I revert a PR after it merges?**

A: Only in emergencies (security issue, major bug). General rule: plan before you commit. If we need to revert, we'll discuss first.

---

## Resources

- **Vector Search**: See `VECTOR_INDEX_GUIDE.md` for deep dive
- **Supabase Setup**: `SUPABASE_SETUP.md`
- **Self-Hosting**: `DOCKER_SETUP.md` (coming soon)
- **License Q&A**: `LICENSE` + `OWNERSHIP.md` + `FREE_TIER_ELIGIBILITY.md`
- **Community**: GitHub Discussions (https://github.com/awanet/pack-dashboard/discussions)

---

## Thank You

Every contribution—code, docs, ideas, encouragement—makes this better.

We're building something real here. Something that serves people, not capital.

Keep it sovereign. 🌱

---

_Questions?_ community@awanet.nz
