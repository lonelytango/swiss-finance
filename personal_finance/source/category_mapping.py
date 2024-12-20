commute_mapping = {
    ('MTA',
    'OMNYPYG',
    'PARKMOBILE',
    'E-Z*PASSNY',
    'PARKING METERS',
    'NSUH PARKING',
    'NYCDOT PARKING'): 'COMMUTE',
}

credit_card_mapping = {
    ('VISA CARD',
    'Online Banking payment',
    'CREDIT CARD',
    'Bill Payment',
    'APPLECARD GSBANK',
    'TD BANK          PAYMENT',
    'CHASE CREDIT CRD'): 'CREDIT CARD'
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
    'BURGER KING',
    'DUNKIN',
    'CROXLEY',
    'ORIENT GARDEN',
    'PIZZA',
    'CHIPOTLE',
    'KABUL GRILL'): 'DINING'
}

entertainment_mapping = {
    ('BESTPRESSO',
     'STEAM PURCHASE',
     'AMC'): 'ENTERTAINMENT',
}

expense_mapping = {
    ('CHECK',
    'SVC CHARGE',
    'NYC FINANCE',
    'DBS BANK',
    'Synchrony Bank'): 'EXPENSE',
}

grocery_mapping = {
    ('SUPERMARKET',
    'SUPER FL MART',
    'MITSUWA',
    'STOP & SHOP',
    'WALGREENS',
    'COSTCO',
    'H MART',
    'TRADER JOE',
    'BIGLOTS'): 'GROCERY'
}

income_mapping = {
    ('E6XUNITED',
    'VENMO',
    'ZELLE FROM',
    'eDeposit',
    'BKOFAMERICA MOBILE',
    'MOBILE DEPOSIT',
    'CASH DEPOSIT',
    'DAILY CASH ADJUSTMENT',
    'IRS TREAS',
    'NYSTTAXRFD',
    'DEPOSIT'): 'INCOME'
}

investment_mapping = {
    ('INTEREST',
     'ROBINHOOD',
     'FID BKG SVC LLC',
     'Monument Metals',
     'GOSABK SV WEBXFR TRANSFER'): 'INVESTMENT',
}

property_mapping = {
    ('NYC DOF DES', 
     'MORTGAGE',
     'WF HOME MTG',
     'ESCROW',
     'PTB Property',
     'TOWN OF HEMPSTEA SERVICE',
     'Property Inc.',
     'EGOV STRATEGIES',
     'NYCPROPTAX'): 'PROPERTY'
}

service_mapping = {
    ('CLASSACTPHOTO',
    'EDUCATION',
    'Zelle Transfer',
    'USPS.COM',
    '*AMERICAN SC',
    'MICROSOFT',
    'TURBOTAX',
    'eBay',
    'Jamie Lin'): 'SERVICE',
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
    'EBAY',
    'CROCS',
    'NESPRESSO',
    'T.J. MAXX',
    'IKEA',
    'BESTBUY',
    'WALMART',
    'LOWES',
    'GAP',
    'Uniqlo',
    'HARRYS',
    'HONGKONGGEE',
    'PADDLE.NET',
    'Zara.com',
    '7-ELEVEN',
    'YAMIBUY',
    'GROUPON',
    'Groupon',
    'BJS WHOLESALE',
    'APPLE.COM',
    'THE HOME DEPOT',
    'UNDER ARMOUR',
    'Nike'): 'SHOPPING'
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
   'Amazon Prime',
   'CAPCUT',
   'Hulu'): 'SUBSCRIPTION'
}

transfer_mapping = {
    ('KEEP THE CHANGE',
    'Online Banking transfer',
    'Move Funds',
    'TD BANK NA DES:ZELLE',
    'ONLINE TRANSFER',
    'SUN XINFANG',
    'WAY2SAVE SAVINGS',
    'APPLE GS SAVINGS',
    'ACH DEPOSIT INTERNET TRANSFER'): 'TRANSFER',
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
    'PAYMENT - THANK YOU',
    'SKIP'): 'SKIP'
}

health_care_mapping = {
  ('NORTHWELL',
   'NATERA',
   'GREAT NECK ENT'): 'HEALTH CARE'
}

combined_mapping = {
  **skip_mapping,
  **commute_mapping,
  **credit_card_mapping,
  **dining_mapping,
  **entertainment_mapping,
  **expense_mapping,
  **health_care_mapping,
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
}

category_mapping = {}
for keys in combined_mapping:
  for key in keys:
    category_mapping[key] = combined_mapping[keys]
