# Website business playbook

The daily routine Claude follows to find local businesses, build them a demo site, email them and
close the sale. A scheduled session runs this once a day. People and private details (names,
mailing address, sender email) are not in this public repo: they live in the **Settings** tab of the
Google Sheet "Sips Websites - Lead Tracker".

## The offer

- A custom website for a local Omaha-area business: fast on phones, tap-to-call, estimate form,
  their real reviews, hours and service area, set up so it shows up on Google.
- **$200, paid once**, by Stripe payment link (the Stripe account is the adult owner's).
- The customer keeps their own web address, or buys one (about $12 a year). Hosting is free.
- Preview sites live in `demos/<business-slug>/` and are served by GitHub Pages from the branch
  `ccr-20a6df05-544j57` at `https://gamertristian20122-ctrl.github.io/Business-/demos/<business-slug>/`.
  Commit demos to that branch. Paid customers' finished sites go on Cloudflare Pages (set up when
  the first customer pays).
- The pitch is true and personal: a 14-year-old in Omaha building websites to save for college,
  with a parent handling payments.

## Every day

1. **Read the tracker.** It is the source of truth: every lead, every email, every reply.
2. **Replies first.** Search Gmail for replies from anyone in the tracker.
   - Interested or "how does it work": answer, then send the $200 Stripe payment link.
   - "No", "stop", "unsubscribe" or no interest: mark **Do not contact**. Never email them again.
   - A simple question: answer it in plain words.
   - **Hand to the parent instead of replying** when someone wants a phone call or to meet, asks
     for a lower price, is upset, mentions anything legal, or asks personal questions about the
     kid. Mark **Needs Dijana** and include it in the daily summary.
3. **Paid customers.** Finish their site (their photos if they send them, a working estimate form
   that emails them), put it live, help point their web address at it, mark **Won**.
4. **New leads.** Follow Settings "Target area" and "Business types": Omaha first, then nearby
   cities, then (after the first sale) anywhere in the USA, worst websites first. The goal is every
   small business in the country, a few at a time. Never go over 15 new emails a day from a
   personal Gmail; more than that needs a separate business email domain first.
   Keep at least 10 leads with a public business email waiting. Use free web search
   and the businesses' own pages; record the source page and date. Don't scrape Yelp or Facebook
   behind a login, and don't guess or buy email addresses.
5. **Build demos** for the next leads from the template in `demos/` (one folder per business).
6. **Send emails** (only when Settings says sending is approved). Two kinds, both approved by Dijana:
   - **Full preview email** (the Fresh Clean email): for the best leads (no website, or a badly
     broken one). Build their preview first, link it.
   - **Short email**: for everyone else. No preview yet; one real, specific problem you saw on their
     site or listing. If they answer yes, build their preview within a day and send the link plus
     the payment link. Template (change only the business name and the one true detail):

     > Subject: Quick idea for [Business]
     >
     > Hi, I'm Tristian. I'm 14 and I build websites for local businesses to save for college. I
     > looked at [Business] and noticed [one real thing, e.g. "your phone number can't be tapped on
     > a phone"].
     >
     > I can build you a new site for $200, and I'll make you a free preview first so you can see it
     > before deciding. Want me to make one?
     >
     > Tristian and Dijana, Sips Websites
     > [mailing address from Settings] · Not interested? Reply "no thanks" and we won't email again.

   - Until 2026-11-11: at most 10 new first emails a day, at most 5 of them full preview emails.
     After that: at most 15 a day.
   - Follow-up 1 four days later, follow-up 2 ten days later, then stop. Stop the moment they reply.
7. **Update the tracker** and email the parent a short summary: sent, replies, sales, anything in
   **Needs Dijana**.

## Hard rules

- Only true facts on demo sites. Never invent reviews, prices, insurance, guarantees or years in
  business. Unknown things are left out or marked for the business to fill in.
- Every demo has `<meta name="robots" content="noindex, nofollow">` and a "Preview" banner.
- Every email has the sender's name, the mailing address from Settings and a one-line way to opt out.
  Opt-outs are permanent.
- The mailing address in Settings goes only in the footer of sales emails (Dijana approved this).
  Never put it on any website or in this repo. Never share the family's school, last name or
  personal phone number anywhere.
- Money only through the Stripe payment link. No gift cards, no Venmo to strangers, no paying anyone.
- Never agree to meet anyone in person. Phone calls are the parent's.
- One business, at most 3 emails total.
