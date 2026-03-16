# Community Model: Revenue Share & Bounties

**Goal**: Make pack-dashboard sustainable while rewarding community contributions and preventing corporate exploitation.

---

## Three Revenue Streams

### 1. Commercial Licenses

**For**: Organizations ≥$1M revenue or ≥10 employees

**Pricing** (flexible, case-by-case):

- Startup/SMB: 1-2% of annual software budget (~$5-20k/year)
- Mid-market: 2-3% of software budget (~$50-100k/year)
- Enterprise: Custom negotiation

**What's included**:

- Perpetual license to deploy modified pack-dashboard
- Optional: support, security patches, consulting
- No open-source requirement (but encouraged)

**Example deal**:

- Company XYZ: $2M annual revenue, 25 employees
- Software budget: $500k/year
- License fee: 2.5% = $12,500/year
- Includes: 8 hours/month support, security updates

### 2. Community Revenue Share

**For**: Organizations using pack-dashboard as core product (SaaS, service offering)

**Model**:

- You use pack-dashboard (free/open-source)
- You agree to share 2-5% of software gross margin
- You open-source code changes (AGPL-3.0 copyleft)
- AwaNet funds: development, hosting, audits

**Tiered rates**:
| Annual Gross Margin | Revenue Share |
|---|---|
| <$100k | 2% |
| $100k - $1M | 3% |
| $1M - $10M | 4% |
| $10M+ | 5% |

**Example**:

- Your SaaS generates $500k annual revenue
- Operating costs: $300k (70%)
- Gross margin: $200k (40%)
- Revenue share: 3% of $200k = $6k/year
- You save: $20-40k vs commercial license
- Pack-dashboard gets: funded development

**Payment**: Quarterly invoices via Stripe or bank transfer

### 3. Community Bounty Fund

**For**: Open-source contributors (bug fixes, features, docs)

**How it works**:

1. **Issues labeled `bounty`** in GitHub repo
2. **Bounty amount posted** (e.g., $100-$1k depending on complexity)
3. **Contributors bid** by commenting on issue
4. **Code merged** → bounty paid (via Stripe, PayPal, or crypto)

**Bounty Categories**:

| Difficulty   | Time Est.   | Bounty    | Examples                                                  |
| ------------ | ----------- | --------- | --------------------------------------------------------- |
| Beginner     | 1-2 hours   | $25-50    | Fix typo, add comment, improve error message              |
| Intermediate | 2-8 hours   | $50-200   | Bug fix, add test, optimize query                         |
| Advanced     | 8-40 hours  | $200-1000 | New feature, complex refactor, performance audit          |
| Research     | 20-80 hours | $500-2000 | Deep investigation, security audit, architecture redesign |

**Eligibility**:

- Any contributor (individuals, teams)
- Must sign CLA (Contributor License Agreement)
- Code must pass review + tests + linting

**Example bounty**:

```markdown
## Bounty: Add Search Filters to PacksTable

**Difficulty**: Intermediate  
**Bounty**: $150  
**Time Est**: 4-6 hours

**Issue**: Users want to filter packs by created_at, metadata tags, embedding similarity threshold.

**Acceptance Criteria**:

- [ ] Add filter controls to PacksTable UI
- [ ] Filter state persists in URL params (?filter=tag:ai&date_from=2025-01-01)
- [ ] Unit tests for filter logic (>80% coverage)
- [ ] ESLint + TypeScript no errors
- [ ] Update CHANGELOG.md

**To Apply**: Comment on this issue with your GitHub profile + estimate.
```

---

## Annual Budget Allocation

**Example**: Year 1 Revenue = $50,000 (mix of licenses + sponsors)

```
$50,000 / Year Budget Breakdown:

Development & Maintenance: $25,000 (50%)
├─ Full-time engineer (4 months @ $6.25k)
├─ Infrastructure (AWS, hosting)
└─ Tools (monitoring, alerting, CI/CD)

Community Bounties: $12,500 (25%)
├─ Bug fixes & features
├─ Documentation
└─ Community projects

Operations & Legal: $7,500 (15%)
├─ Accounting & tax
├─ License enforcement
├─ Security audits

Reserves & Growth: $5,000 (10%)
├─ Unexpected costs
└─ Reinvest in sustainability
```

**Published annually** in `TRANSPARENCY.md` (every January 1)

---

## How to Apply for Bounties

### Step 1: Choose an Issue

Visit: `https://github.com/awanet/pack-dashboard/issues?labels=bounty`

Look for:

- Difficulty matching your skill level
- Bounty amount you find motivating
- Feature/area you care about

### Step 2: Comment on Issue

```
## Bounty Application

**GitHub**: @yourhandle
**Estimate**: 6 hours
**Experience**: 5 years TypeScript, contributed to [Project1, Project2]
**Timeline**: Can start next week, finish in 10 days

I'd love to work on this. [Brief explanation why you're a good fit]

Any questions before I start? @awanet/maintainers
```

### Step 3: Wait for Approval

Maintainers will reply within 48 hours:

- ✅ Approved → start coding (on your fork)
- ⏳ Waiting list → others applied first, we'll loop back if they drop out
- ❌ Not selected → feedback on why, invited to apply for other bounties

### Step 4: Code & Submit PR

- Fork pack-dashboard repo
- Create branch: `bounty/[issue-id]-[description]`
- Code with quality in mind (see `CONTRIBUTING.md`)
- Push to GitHub, open Pull Request
- Link PR to bounty issue: `Closes #123`

### Step 5: Review & Merge

- Maintainers review code (3-5 business days)
- Feedback on style, tests, docs
- You iterate until approved
- PR merged → bounty paid within 7 days

### Step 6: Get Paid

**Payment options** (choose one):

1. **Stripe**: Instant (credit/debit card)
2. **PayPal**: 1-2 days
3. **Crypto**: Instant (Bitcoin, Ethereum)
4. **Donated to Charity**: We donate on your behalf (tax deductible for us)

**Form**: Send to bounty@awanet.nz with:

```
Contributor Name: [Legal name for payment]
GitHub: @yourhandle
Issue: #[number]
Amount: $[bounty amount]
Payment Method: [Stripe / PayPal / Crypto / Charity]
Payment Details: [Email, crypto address, or charity name]
```

---

## Sponsorship Tiers

**For organizations wanting to support pack-dashboard directly**

### Gold Sponsor ($5,000/year)

- Logo on README.md + website
- Monthly update call with maintainers
- Priority feature requests (within reason)
- Co-branded blog post

### Silver Sponsor ($2,000/year)

- Logo on README.md
- Quarterly update
- Early access to features

### Bronze Sponsor ($500/year)

- Mention on SPONSORS.md
- Early release notifications

**How to sponsor**: Email partnerships@awanet.nz

---

## Grant Funding

We apply for grants to fund public benefit work:

**Sources pursued**:

- Shuttleworth Foundation (open-source + social impact)
- NLnet (internet infrastructure)
- EU Horizon Europe (open-source tools)
- Mozilla Foundation (internet health)
- Sloan Foundation (tech for public good)

**How grants are used**:

- Full-time dev time (not funded by licenses)
- Security audits & penetration testing
- Community outreach (free tier marketing)
- Accessibility improvements
- Internationalization (translations)

**Grant announcements**: See blog + GRANTS.md

---

## Why This Model?

### For Individuals & Non-Profits

- **Free tier stays free** (no surprise paid gates)
- **Bounties let you earn** while contributing
- **Community funded** (not VC-backed, no exit pressure)
- **Transparent allocation** (you see where money goes)

### For Companies

- **Fair pricing** (not exploitative SaaS markups)
- **Open-source option** (pay only if you want proprietary deployment)
- **Revenue-share partnership** (grow together)
- **Predictable costs** (no surprises)

### For AwaNet

- **Sustainable** (no need to sell user data or ads)
- **Community-aligned** (revenue comes from value we create)
- **Scalable** (licenses + sponsorships + bounties)
- **Ethical** (no extraction, just collaboration)

---

## FAQ

**Q: Do I have to contribute to earn recognition?**

A: No! Using pack-dashboard, spreading the word, giving feedback — all valuable. Bounties are just one way to be rewarded.

**Q: Can I apply for multiple bounties?**

A: Yes! One at a time (we try to queue you fairly). Experienced contributors can do 2-3 simultaneously.

**Q: What if I don't finish the bounty in time?**

A: Let us know ASAP. We'll either extend the deadline or reassign. No penalties — life happens.

**Q: Can companies participate in bounties?**

A: Yes, but we prioritize individual contributors. If a company wants bulk bounty work, contact: partnerships@awanet.nz

**Q: How is the Contributor License Agreement (CLA) different from AGPL-3.0?**

A: CLA grants AwaNet copyright rights to your code (so we can dual-license or relicense if needed). AGPL-3.0 is the public license for all users. CLA doesn't restrict you — it protects us from fragmentation.

**Q: Can I bundle my bounty earnings for a bulk payment?**

A: Absolutely. Complete multiple bounties, then request payment in one batch.

**Q: What if someone cheats (ghost-codes, plagiarizes)?**

A: Banned from bounty program + referred to legal (depending on severity). We verify code via review + plagiarism checking.

---

## Current Sponsors

(This section will grow!)

- 🏛️ **Charity Name TBD** (Silver Tier, 2025)

---

## Transparency Links

- **Bounties**: GitHub Issues labeled `bounty`
- **Annual Budget**: `TRANSPARENCY.md`
- **Commercial Licenses**: Anonymized metrics in annual report
- **Contributors**: `CONTRIBUTORS.md`

---

## Apply Now

- **Free Tier**: See `FREE_TIER_ELIGIBILITY.md`
- **Want a Bounty?**: Check GitHub issues
- **Want to Sponsor?**: Email partnerships@awanet.nz
- **Have Ideas?**: Open an issue or email policy@awanet.nz

---

**Keep it community-owned. Keep it fair.** 🌱
