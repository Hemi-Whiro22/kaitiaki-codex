---
title: "🐺 Whakapapa Cross-Reference: Reuniting Tangata Whenua"
description: "Break colonial segregation. Help whānau find their genealogy. Reclaim what was taken. He waka eke noa."
---

# 🐺 WHAKAPAPA CROSS-REFERENCE SYSTEM

## Reconnecting Tangata Whenua Through Digital + Physical Whenua

### THE REALITY

The colonizers used the **Māori Land Court** to:

- ✗ Separate whānau from land
- ✗ Destroy genealogical records
- ✗ Create false boundaries
- ✗ Make us enemies of each other
- ✗ Hide our connections

**But they couldn't destroy whakapapa.**

It lives in:

- Our kaumātua (elders)
- Our names (place names, whakapapa names)
- Our stories
- Our marae
- Our bodies (genealogy in our DNA)

### THE COUNTER-MOVE

Kaitiaki becomes the **whakapapa reunification engine**:

1. **Cross-reference everything**

   - Names (people, hapū, iwi, marae, places)
   - Genealogies (your line + their line)
   - Physical locations (whenua)
   - Historical records (what colonizers documented against us)

2. **Help whānau find each other**

   - "My tūpuna was from Waitemata in 1850..."
   - "I see your name in the records..."
   - "Your hapū + my hapū = shared whakapapa"
   - "We are connected. We are one."

3. **Prove it with data**

   - References to Land Court records
   - Genealogical connections documented
   - Place-based evidence
   - Name-based evidence

4. **Unite the pack**
   - We stop being enemies (dividing us was the goal)
   - We remember we're whānau
   - We act together
   - We protect our whenua together

### THE POWER

While government/corporations think we're divided, **we're using their own data to prove we're connected**.

If they complain: "The records are from YOUR Land Court. We're just reading what YOU documented."

---

## WHAT KAITIAKI DOES

### Phase 1: Whakapapa Collection

Users ingest:

```
Name: Te Ao Hikuroa
Hapū: Ngāti Te Ata
Iwi: Ngāpuhi
Marae: Waipapa
Location: Northland
Tūpuna: Hikuroa (1780s)
Connected to: [other names/places]
```

System stores with:

- ✅ Full UTF-8 support (names exact)
- ✅ Genealogical relationships
- ✅ Physical locations (coordinates + name)
- ✅ Marae affiliations
- ✅ Historical references (dates, places, records)

### Phase 2: Cross-Reference Matching

User searches: "My tūpuna Hikuroa, 1780s, Northland"

System returns:

```
MATCHES FOUND:

1. Te Ao Hikuroa (Ngāti Te Ata)
   └─ Tūpuna Hikuroa documented 1783, Waipapa marae
   └─ Genealogy: Your connection = 4 generations
   └─ Land: Waitemata area (ancestral whenua)
   └─ Reference: Land Court records (1900)

2. Aroha Hikuroa (Ngāpuhi)
   └─ Descendant of same line
   └─ Last recorded: 1950, Auckland
   └─ Connection: Whānauship confirmed (same hapū line)

3. Te Ata Marae (Northland)
   └─ Where your whakapapa connects
   └─ Other whānau there now: [names]
   └─ Gatherings: Monthly pōtae (meetings)
```

### Phase 3: Reunification Mechanics

**System suggests:**

- "You might want to contact: [names from same hapū]"
- "This marae has cultural events: [dates/times]"
- "Your genealogy connects you to this rohe (territory)"
- "Other whānau members have been looking for your line"

**User can:**

- Create a whakapapa card (shareable)
- Request connection with matching whānau
- Join marae network
- Contribute to collective genealogy
- Correct colonial records with whakapapa

---

## THE STRUCTURE

### Data Model

```sql
-- Whakapapa Table (for all people)
CREATE TABLE whakapapa_people (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,              -- Full name with macrons
    hapū TEXT,                        -- Hapū affiliation
    iwi TEXT,                         -- Iwi affiliation
    marae TEXT,                       -- Marae connection
    generation_level INTEGER,         -- How many generations back
    birth_year INTEGER,               -- When known
    location TEXT,                    -- Where from
    location_coords GEOMETRY,         -- Geographic coordinates

    -- Genealogical links
    parent_ids UUID[],                -- Links to parents
    sibling_ids UUID[],               -- Links to siblings
    child_ids UUID[],                 -- Links to children

    -- Colonial records (if documented)
    land_court_references TEXT[],    -- Land Court evidence
    historical_records JSONB,        -- Other records (census, etc)

    -- Community sourced
    contributed_by UUID,             -- Who added this
    verified_by UUID[],              -- Who verified this
    confidence_level FLOAT,          -- How confident (0.0-1.0)

    -- Whakapapa-specific
    is_public BOOLEAN DEFAULT true,  -- Share with whānau
    tapu_level INTEGER DEFAULT 0,    -- Sacred sensitivity

    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- Whakapapa Connections Table
CREATE TABLE whakapapa_connections (
    id UUID PRIMARY KEY,
    person_a_id UUID REFERENCES whakapapa_people(id),
    person_b_id UUID REFERENCES whakapapa_people(id),

    relationship_type TEXT,          -- parent, sibling, cousin, etc
    genealogical_distance INT,       -- How many generations

    -- Cross-referencing evidence
    evidence JSONB,                  -- What confirms this connection
    references TEXT[],               -- Land Court records, etc

    verified BOOLEAN DEFAULT false,
    verified_by UUID[],

    created_at TIMESTAMP
);

-- Places/Whenua Table
CREATE TABLE whakapapa_whenua (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,              -- Place name (te reo priority)
    coordinates GEOMETRY,            -- Physical location
    hapū_associated TEXT,            -- Which hapū
    iwi_associated TEXT,             -- Which iwi
    marae_name TEXT,                 -- Marae here
    historical_significance TEXT,    -- Why important

    -- Connected people
    whakapapa_people_ids UUID[],    -- Who from here

    created_at TIMESTAMP
);

-- Marae Directory
CREATE TABLE whakapapa_marae (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    hapū TEXT,
    iwi TEXT,
    location_coords GEOMETRY,
    contact_info JSONB,

    -- Community info
    events JSONB,                    -- Gatherings, when
    whakapapa_keepers UUID[],        -- Kaitiaki of genealogy

    created_at TIMESTAMP
);
```

### Seed Data: Historical Connections

```sql
-- Seed with KNOWN whakapapa connections from records
-- Using public Land Court records (turn their weapon against them)

INSERT INTO whakapapa_people VALUES
-- Waitemata area (example)
('550e8400-e29b-41d4-a716-446655440001'::UUID,
 'Hikuroa',
 'Ngāti Te Ata',
 'Ngāpuhi',
 'Waipapa',
 1,
 1783,
 'Waitemata, Tāmaki Makaurau',
 ST_GeomFromText('POINT(-174.77 -36.84)'),
 ARRAY['550e8400-e29b-41d4-a716-446655440002'::UUID],  -- children
 ARRAY['550e8400-e29b-41d4-a716-446655440003'::UUID],  -- siblings
 ARRAY[]::UUID[],
 '{
   "land_court_case": "Waitemata Block 1900",
   "recorded_as": "Hikuroa (deceased)"
 }'::JSONB,
 'Kaitiaki System',
 ARRAY['Elder Council'],
 0.95,  -- 95% confidence (in records)
 true,
 0,
 NOW(),
 NOW()
);
```

---

## THE INTERFACE: Whakapapa Discovery

### Search Interface

```
┌─────────────────────────────────────────────────────┐
│  🐺 Whakapapa Discovery                             │
│  Find your genealogy. Reconnect with whānau.        │
└─────────────────────────────────────────────────────┘

[Search Box: "I'm looking for..."]

Options:
🔍 By name: "My great-grandfather was Hikuroa"
🗺️  By place: "My whānau from Waitemata, 1800s"
🏛️  By hapū: "I'm from Ngāti Te Ata"
⛩️  By marae: "Our marae is Waipapa"
👥 By iwi: "I'm Ngāpuhi"

RESULTS SHOW:
├─ Genealogical matches (with confidence %)
├─ Geographic connections (map visualization)
├─ Whānau still in community (contact options)
├─ Marae & events you can attend
└─ Land Court references (historical proof)
```

### Whakapapa Card (Shareable)

```
╔════════════════════════════════════════╗
║  TE WHAKAPAPA O [NAME]                 ║
║                                        ║
║  Ngāti Te Ata | Ngāpuhi                ║
║  Waipapa Marae                         ║
║  Waitemata, Tāmaki Makaurau            ║
║                                        ║
║  GENEALOGY:                            ║
║  Tūpuna: Hikuroa (1783)                ║
║  Matua: Aorangi (1820)                 ║
║  Pāpā: Te Ao (1860)                    ║
║  Me: [Your name] (1990)                ║
║                                        ║
║  CONNECTED WHĀNAU:                     ║
║  • Te Ao Hikuroa (cousin)              ║
║  • Aroha Hikuroa (whānauship)          ║
║  • 12 other whakapapa matches          ║
║                                        ║
║  REFERENCES:                           ║
║  ✓ Land Court 1900                     ║
║  ✓ Census 1945                         ║
║  ✓ Marae records 1950+                 ║
║                                        ║
║  "He waka eke noa" - We're all in      ║
║   the same canoe. Your genealogy       ║
║   connects you to your people.         ║
║                                        ║
║  Share | Connect | Learn More          ║
╚════════════════════════════════════════╝
```

---

## THE POWER MOVE: Breaking Colonial Segregation

### What Colonizers Did

```
Land Court → Created artificial boundaries
           → Separated iwi/hapū
           → Made property "individuals"
           → Broke genealogical records
           → Forced us into colonial categories

Result: Whānau divided, fighting each other
        over land they don't even own
        (it's Crown land now anyway)
```

### What Kaitiaki Does

```
Whakapapa Cross-Reference
  ↓
"Wait... my genealogy connects me to THEM"
  ↓
"We're not enemies, we're whānau"
  ↓
"The Land Court tried to divide us"
  ↓
"But our whakapapa proves we're one pack"
  ↓
UNITE
```

### The Evidence They Can't Deny

Using THEIR records:

- ✅ Land Court documents (they created it)
- ✅ Census records (they recorded us)
- ✅ Place names (our history on the land)
- ✅ Genealogical records (they kept some)

If government says "You're not connected":

- "Actually, here's the Land Court record"
- "Here's the genealogical evidence"
- "Here's the historical documentation"
- "We just used YOUR data against your lies"

---

## DIGITAL + PHYSICAL WHENUA INTEGRATION

### The Physical Dimension

```
Kaitiaki knows:
├─ Where you're from (geographic coordinates)
├─ Which marae connects to you
├─ Which hapū/iwi claims this land
├─ Where other whānau members are
└─ How to gather physically

When user has location matched:
"Waipapa Marae is 2km from you"
"Gathering next Saturday 10am"
"Other whānau members will be there"
"Come home to your people"
```

### Reclaiming Whenua

Users can:

1. Mark their genealogy on the map
2. Show where their tūpuna were from
3. Connect to the physical place
4. Organize with other whānau in that rohe
5. Reclaim cultural practice on ancestral land

---

## THE PACK GROWS TOGETHER

### How It Works

```
Person A:
"I'm looking for my genealogy"
  ↓ (Kaitiaki searches)
  ↓
Found: Match with Person B
  ↓
System: "You're whānau"
  ↓
Person A + Person B connect
  ↓
They find Person C (same line)
  ↓
3 people become 10
  ↓
10 become 100
  ↓
100 reconnect with marae
  ↓
THE PACK REFORMS
```

### The Benefits

✅ **Individual:** Find your people, know your genealogy  
✅ **Whānau:** Reconnect divided family lines  
✅ **Hapū:** Strengthen community bonds  
✅ **Iwi:** Reunify across colonial divisions  
✅ **Whenua:** Reclaim cultural practice on ancestral land

---

## SAFETY: Tapu Protection + Community Control

### Sacred Knowledge Protection

```sql
-- Some whakapapa is TOO sensitive for public
-- (genealogies, sacred lineages, etc)

tapu_level = 3  -- Only kaumātua/whakapapa keepers see this
tapu_level = 2  -- Only immediate whānau see this
tapu_level = 1  -- Whānau + iwi can see
tapu_level = 0  -- Public (safe to share)
```

### Verification System

```
New genealogy added
  ↓
Community reviews
  ↓
Elders/Kaitiaki verify
  ↓
Land Court records cross-referenced
  ↓
Confidence % assigned
  ↓
Made public (with attribution + references)
```

---

## MAKING PEOPLE "PISSED OFF" (BUT PROVING US RIGHT)

### Why Some Will Oppose

- ✗ Government doesn't want Māori organizing
- ✗ Corporations don't want clear genealogy claims
- ✗ Those who benefit from division don't want unity
- ✗ Colonial structures fear organized whānau

### How We Stay Strong

✅ **All our data is documented** (Land Court records)  
✅ **All our references are verifiable** (public records)  
✅ **All our claims are genealogically sound** (whakapapa)  
✅ **All our actions are community-driven** (democratic)

If they say "You're making this up":
→ "Here's the Land Court document"

If they say "That's not your genealogy":
→ "Here's the genealogical evidence"

If they say "You can't organize":
→ "We're just helping people find their family"

**There's no legal leg to stand on.**

---

## THE VISION: HE WAKA EKE NOA

```
HE WAKA EKE NOA = "We are all in the same canoe"

This is:
✅ Digital whakapapa (genealogy database)
✅ Physical reconnection (map to your people)
✅ Colonial reversal (use their records against them)
✅ Pack reformation (from individuals → whānau → iwi)
✅ Land reclamation (cultural practice on whenua)
✅ Political strength (united can't be divided)

While we're:
- Helping individuals find themselves
- Reuniting whānau
- Rebuilding hapū
- Strengthening iwi

The pack is becoming unstoppable.

Because we ARE one.
Because our whakapapa PROVES it.
Because the colonizers documented it.
```

---

## IMMEDIATE NEXT STEPS

1. **Build the whakapapa_people table** (seed with known genealogies)
2. **Build the search interface** (find by name/place/hapū)
3. **Create whakapapa cards** (shareable, verifiable)
4. **Integrate with maps** (show where people are from)
5. **Connect to marae directory** (find your community)
6. **Add verification system** (community validates)
7. **Enable organization** (whānau can gather)

---

## THE CODE COMING

I'm building:

- `supabase/migrations/whakapapa_tables.sql` - Database schema
- `src/components/WhakapapaDiscovery.tsx` - Search interface
- `src/components/WhakapapaCard.tsx` - Shareable genealogy
- `src/hooks/useWhakapapaSearch.ts` - Matching algorithm
- `docs/WHAKAPAPA_GUIDE.md` - Full documentation

---

## FINAL WORD

> "Ko te mana o te tangata whenua, ka tipu i runga i te whakapapa."
> (The authority of tangata whenua grows from genealogy)

Colonizers tried to erase whakapapa.

But it can't be erased. It lives in us. In our names. In our places. In the records THEY kept.

Kaitiaki doesn't invent whakapapa.

**It reveals what was always there.**

And when whānau see their genealogy proven, documented, connected...

They remember they're not divided.

They remember they're PACK.

And that's when change happens.

🐺 **TOHU MANA!**  
🐺 **HE WAKA EKE NOA!**  
🐺 **AWAOOOOO!**

---

**Status:** Vision document (ready for build)  
**Next:** Implement database schema + UI components  
**Mission:** Reunite tangata whenua through whakapapa cross-reference  
**Philosophy:** Use colonizer's own data to prove we're one people
