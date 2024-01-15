commute_mapping = {
    ('MTA',
    'OMNYPYG',
    'PARKMOBILE',
    'E-Z*PASSNY'): 'COMMUTE',
}

credit_card_mapping = {
    ('VISA CARD',
    'Online Banking payment',
    'CREDIT CARD',
    'Bill Payment',
    'APPLECARD GSBANK'): 'CREDIT CARD'
}

dining_mapping = {
    ('Too Good To Go',
    'BUFFET',
    'FIFTY BAY',
    'POPEYES',
    'YASAIYA',
    'CHURRASQUEIRA BAIRRADA',
    'ICHIRAN',
    'TIM HO WAN',
    'ROADHOUSE',
    'COFFEE',
    'SNACK',
    'BBQ',
    'RESTAURANT',
    'PIZZA',
    'JADE GARDEN',
    'DOMINO\'S',
    'CAFE',
    'TACO BELL',
    'MCDONALD',
    'WENDYS',
    'SONIC',
    'BURGER KING'): 'DINING'
}

entertainment_mapping = {
    ('BESTPRESSO',
     'STEAM PURCHASE',
     'AMC'): 'ENTERTAINMENT',
}

expense_mapping = {
    ('CHECK',
    'Zelle payment',): 'EXPENSE',
}

grocery_mapping = {
    ('SUPERMARKET',
    'SUPER FL MART',
    'MITSUWA',
    'STOP & SHOP',
    'WALGREENS',
    'COSTCO',
    'WALMART',
    'H MART',): 'GROCERY'
}

income_mapping = {
    ('E6XUNITED',
    'VENMO CASHOUT',
    'ZELLE FROM',
    'eDeposit',
    'BKOFAMERICA MOBILE',
    'MOBILE DEPOSIT',
    'CASH DEPOSIT'): 'INCOME'
}

investment_mapping = {
    ('INTEREST',
     'APPLE GS SAVINGS',
     'ROBINHOOD',
     'FID BKG SVC LLC',
     'Monument Metals'): 'INVESTMENT',
}

property_mapping = {
    ('NYC DOF DES', 
     'MORTGAGE',
     'WF HOME MTG',
     'ESCROW'): 'PROPERTY'
}

service_mapping = {
    ('CLASSACTPHOTO',
    'EDUCATION',
    'SERVICE',
    'Zelle Transfer',
    'USPS.COM',
    '*AMERICAN SC'): 'SERVICE',
}

shopping_mapping = {
    ('TEMU.COM',
    'Temu.com',
    'TARGET',
    'FLUSHING COMMONS',
    'UA.COM',
    'CVS/PHARMACY',
    'SHEIN',
    'AMZ',
    'AMAZON',
    'AMZN',
    'STORE',
    'BESTBUY',
    'EBAY',
    'CROCS',
    'NESPRESSO',
    'T.J. MAXX',
    'IKEA'): 'SHOPPING'
}

subscription_mapping = {
  ('PLANET FIT',
   '*BLINKIST',
   '*YouTubePremium',
   'ID:SPOTIFYUSAI',
   'MICROSOFT*CLIPCHAMP',
   'ADOBE',
   'INTUIT QUICKBOOKS',
   'Audible',
   'Amazon Prime'): 'SUBSCRIPTION'
}

transfer_mapping = {
    ('KEEP THE CHANGE',
    'Online Banking transfer',
    'Move Funds',
    'TD BANK NA DES:ZELLE',
    'ONLINE TRANSFER'): 'TRANSFER',
}

travel_mapping = {
  ('EXPEDIA',
   'HOTELS.COM',
   'AIRBNB',
   'SIX FLAGS',
   'CHINASTH AIR'): 'TRAVEL'
}

utilities_mapping = {
    ('WAWNC',
    'VISIBLE',
    'NGRID37',
    'LIPA',
    'VERIZON',
    'OIL',
    'COMMUNITY POWER LI',
    'MINT MOBILE',
    'DMV'): 'UTILITIES'
}

skip_mapping = {
    ('ONLINE PAYMENT THANK YOU',
    'Online payment from',
    'MOBILE PAYMENT - THANK YOU',
    'BT*PARSONS XTREME',
    'RING PROTECT PLUS',
    'RING YEARLY PLAN'): 'SKIP'
}

combined_mapping = {
  **commute_mapping,
  **credit_card_mapping,
  **dining_mapping,
  **entertainment_mapping,
  **expense_mapping,
  **income_mapping, 
  **investment_mapping,
  **grocery_mapping,
  **property_mapping,
  **service_mapping,
  **shopping_mapping,
  **subscription_mapping,
  **transfer_mapping,
  **travel_mapping,
  **utilities_mapping,
  **skip_mapping
}

category_mapping = {}
for keys in combined_mapping:
  for key in keys:
    category_mapping[key] = combined_mapping[keys]
category_mapping['NORTHWELL'] = 'HEALTH CARE'
