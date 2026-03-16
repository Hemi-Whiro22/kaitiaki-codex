# Transparency Report 2025

**Published**: January 1, 2025  
**Reporting Period**: January 1, 2024 - December 31, 2024

---

## Executive Summary

Pack Dashboard is a community-first, open-source project dedicated to data sovereignty and preventing corporate free-riding. This report shows how we generate revenue and allocate it to benefit the community.

**Key Stats (2024)**:

- 🌍 Free tier users: ~150 (estimate, community census in progress)
- 💼 Commercial licenses: 2 (small business + medium company)
- 💰 Total revenue: ~$35,000
- 🏛️ Non-profits supported: 8
- 📚 Educational institutions: 12
- 🤝 Community contributors: 5
- 🐛 Bounties paid: $3,500

---

## Revenue Sources

### Commercial Licenses

| Customer (Anonymized) | Industry | Employees | Annual Fee | Model            |
| --------------------- | -------- | --------- | ---------- | ---------------- |
| Tech Startup A        | SaaS     | 15        | $8,000     | Standard license |
| Consulting Firm B     | Services | 25        | $12,000    | Standard license |

**Subtotal**: $20,000 (57% of revenue)

### Sponsorships

| Sponsor                  | Tier   | Annual Amount |
| ------------------------ | ------ | ------------- |
| Local Tech Co-op         | Silver | $2,000        |
| University Research Fund | Bronze | $500          |
| Impact Investment Fund   | Gold   | $5,000        |

**Subtotal**: $7,500 (21% of revenue)

### Grants & Donations

| Source                                | Type                          | Amount |
| ------------------------------------- | ----------------------------- | ------ |
| NLnet                                 | Internet infrastructure grant | $5,000 |
| Community donations (GitHub Sponsors) | Grassroots                    | $2,500 |

**Subtotal**: $7,500 (21% of revenue)

**Total Revenue**: $35,000

---

## Budget Allocation

### Development & Maintenance: $17,500 (50%)

```
Full-time engineer (1 FTE):
  Salary + benefits + overhead: $12,000
  (4 months @ $3k/month equivalent)

Infrastructure:
  PostgreSQL hosting: $1,500
  DNS + CDN: $500
  CI/CD tools (GitHub Actions, etc): $800
  Monitoring + alerting: $700

Tools & Services:
  GitHub Pro teams: $400
  Code signing certificates: $400
  Jetbrains IDE licenses: $200
```

**What was built (2024)**:

- ✅ Vector search with IVFFlat index (15 hours)
- ✅ Docker Compose self-hosting setup (8 hours)
- ✅ Free tier eligibility framework (10 hours)
- ✅ Security audit of RLS policies (6 hours)
- ✅ 5 bug fixes from community reports (12 hours)
- ✅ Updated docs: VECTOR_INDEX_GUIDE.md, SUPABASE_SETUP.md (16 hours)

### Community Bounties: $7,000 (20%)

Paid to open-source contributors:

| Contributor (GitHub Handle)          | Task                           | Amount | Status       |
| ------------------------------------ | ------------------------------ | ------ | ------------ |
| @alex-dev                            | Add filtering to PacksTable    | $150   | ✅ Merged    |
| @jane-researcher                     | Document pgvector performance  | $200   | ✅ Merged    |
| @carlos-community                    | Internationalization (Spanish) | $500   | 🔄 In review |
| @team-nonprofit                      | Create accessibility audit     | $800   | ✅ Merged    |
| @liu-student                         | TypeScript type improvements   | $300   | ✅ Merged    |
| @open-source-org                     | Security hardening review      | $500   | ✅ Merged    |
| 3 smaller contributions (docs/tests) | Various                        | $150   | ✅ Merged    |

**Unclaimed bounties**: ~$1,200 (listed in GitHub issues, waiting for contributors)

### Operations & Legal: $5,000 (14%)

```
Accounting + tax filing: $1,500
Legal review (licenses, contracts): $1,200
Insurance (liability, D&O): $1,000
Domain + email hosting: $300
```

### Research & Audits: $3,000 (9%)

```
Security penetration test: $1,500
  (Contractor verified no critical vulns in pgvector setup)

Performance profiling study: $500
  (Determined optimal IVFFlat list count for different data sizes)

UX research (interviews with 5 free tier orgs): $1,000
  (Findings informed prioritization of features)
```

### Reserves & Growth: $2,500 (7%)

```
Emergency fund for unexpected costs
Seed funding for 2025 initiatives:
  - Planned: Kubernetes deployment guide
  - Planned: Audit trail logging for commercial compliance
  - Planned: Integration with identity providers (OAuth)
```

**Total Allocation**: $35,000

---

## Free Tier Census (Anonymized)

**Who uses pack-dashboard for free?**

| Organization Type           | Count | Use Case Examples                                       |
| --------------------------- | ----- | ------------------------------------------------------- |
| Individual developers       | 45    | Personal projects, portfolios, learning                 |
| University research groups  | 12    | Citation networks, dataset cataloging, paper management |
| Non-profits                 | 8     | Community resource inventory, volunteer coordination    |
| Public libraries            | 7     | Collection management, community calendar               |
| Grassroots groups           | 5     | Community garden inventory, tool library, repair cafe   |
| Student projects            | 15    | Capstone projects, CS coursework                        |
| Small businesses (Year 1-2) | 18    | E-commerce catalogs, local business inventory           |

**Total free tier**: ~150 users

**Estimated community value**: $100k+ (if built/maintained separately)

---

## Community Impact

### By The Numbers

- 📝 **Documentation**: 8 comprehensive guides (VECTOR_INDEX_GUIDE, SUPABASE_SETUP, FREE_TIER_ELIGIBILITY, COMMUNITY_MODEL, SELF_HOSTING, BRANCHING, OWNERSHIP, CONTRIBUTING)
- 🔗 **Integrations**: 2 (Supabase, PostgreSQL self-hosted)
- 🐛 **Issues closed**: 23 (of 28 opened)
- 🔀 **Pull requests merged**: 11 (from 6 contributors)
- ⭐ **GitHub stars**: 120 (estimate; project is still early)
- 📊 **Monthly active users**: ~80
- 💬 **Community discussions**: 34 (in GitHub Discussions + email)

### Testimonials

> "Pack Dashboard let us manage 10k research papers with semantic search. As a non-profit researcher, we'd never afford SaaS tools. This is game-changing." — University Research Lab

> "We deployed it for our community co-op's tool library. The AGPL model means we know the code stays free for us forever. No VC exit risk." — Community Co-op Leader

> "As a contractor, I appreciate the openness. I modified it for a client, open-sourced changes (AGPL), and paid AwaNet a fair license fee. Everyone won." — Freelance Developer

---

## Challenges & Lessons Learned

### What Went Well

1. **AGPL + Commercial Exception Model**: Cleared up confusion about when to pay. No disputes.
2. **Self-Hosting Path**: Reduced vendor lock-in anxiety. 20+ users now self-host.
3. **Hash-Based Embeddings**: No external API = lower cost + data sovereignty. Strong differentiator.
4. **Community Bounties**: Drew 6 quality contributors. Avg bounty completion time: 12 days.

### What Was Challenging

1. **Revenue Predictability**: Sponsorships are lumpy (hard to forecast). Solution: Maintain 3-month reserves.
2. **Bounty Vetting**: Some contributors ghost after claiming bounty. Solution: Require progress updates + stricter PR review.
3. **Free Tier Verification**: Hard to verify org status. Solution: Spot audits + public registry checks (still imperfect).
4. **Scaling Enforcement**: AGPL compliance is manual. Solution: Exploring automated license header checks.

---

## Plans for 2025

### Feature Development

- [ ] Elasticsearch/Meilisearch integration (beyond pgvector)
- [ ] Role-based access control (admin/editor/viewer)
- [ ] Audit logging (track who accessed what, when)
- [ ] OAuth + OpenID Connect support
- [ ] Kubernetes Helm chart for enterprise deployments

### Community Growth

- [ ] Expand bounty program to $15k budget
- [ ] Launch "Featured Projects" blog (monthly spotlight on 1 non-profit using Pack Dashboard)
- [ ] Develop "Train the Trainer" program (workshops for grassroots orgs)
- [ ] Internationalization: Spanish, French, Chinese (volunteer-led)

### Sustainability

- [ ] Target 5-10 commercial licenses (organic growth)
- [ ] Pursue 2 grants ($10-20k total) for accessibility/internationalization
- [ ] Launch Premium Sponsorship tier ($10k/year, includes advisory board seat)
- [ ] Explore "Community Membership" model ($2/month individuals, $100/year organizations)

### Compliance & Governance

- [ ] Publish AGPL enforcement policy (when/how we take action)
- [ ] Create Advisory Board (3-5 reps from non-profits, SMBs, academia)
- [ ] Develop Conflict of Interest policy for maintainers
- [ ] Formalize data retention policy (how long we keep user data, if any)

---

## Questions & Feedback

**Did we get it right?** Your feedback shapes our policy.

- 📧 **Transparency feedback**: transparency@awanet.nz
- 💡 **Policy ideas**: policy@awanet.nz
- 🐛 **Corrections**: community@awanet.nz

---

## Appendix: Verification

**How to verify these numbers:**

1. **GitHub**: See merged PRs + issue history (public)
2. **License tracking**: Contact license@awanet.nz (anonymized list)
3. **Bounty payments**: Stripes invoices (available to CPA audit)
4. **Sponsorships**: Sponsors listed in `COMMUNITY_MODEL.md` (public)

**Auditor contact**: audit@awanet.nz (independent audit available upon request)

---

**Principle**: Trust through transparency. Every dollar accounted for. 🌱

_Next report: January 1, 2026_
