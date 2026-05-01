from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import Flowable
import reportlab.rl_config

# ── colours ──────────────────────────────────────────────────────────────────
DARK_BLUE   = colors.HexColor("#1a237e")
MED_BLUE    = colors.HexColor("#283593")
LIGHT_BLUE  = colors.HexColor("#e8eaf6")
ACCENT      = colors.HexColor("#0288d1")
ACCENT_LIGHT= colors.HexColor("#e1f5fe")
GREEN       = colors.HexColor("#1b5e20")
GREEN_LIGHT = colors.HexColor("#e8f5e9")
ORANGE      = colors.HexColor("#e65100")
ORANGE_LIGHT= colors.HexColor("#fff3e0")
RED         = colors.HexColor("#b71c1c")
RED_LIGHT   = colors.HexColor("#ffebee")
YELLOW_LIGHT= colors.HexColor("#fffde7")
GREY        = colors.HexColor("#424242")
LIGHT_GREY  = colors.HexColor("#f5f5f5")
WHITE       = colors.white
BLACK       = colors.black

W, H = A4

# ── styles ────────────────────────────────────────────────────────────────────
base = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, **kw)

COVER_TITLE = S("CoverTitle", fontSize=28, textColor=WHITE, alignment=TA_CENTER,
                fontName="Helvetica-Bold", leading=34, spaceAfter=8)
COVER_SUB   = S("CoverSub",  fontSize=14, textColor=colors.HexColor("#b3e5fc"),
                alignment=TA_CENTER, fontName="Helvetica", leading=18)
COVER_TAG   = S("CoverTag",  fontSize=11, textColor=colors.HexColor("#ffe082"),
                alignment=TA_CENTER, fontName="Helvetica-Bold")

UNIT_TITLE  = S("UnitTitle", fontSize=22, textColor=WHITE, alignment=TA_CENTER,
                fontName="Helvetica-Bold", leading=28, spaceAfter=4)
UNIT_SUB    = S("UnitSub",   fontSize=11, textColor=colors.HexColor("#b3e5fc"),
                alignment=TA_CENTER, fontName="Helvetica")

H1 = S("H1", fontSize=16, textColor=WHITE, fontName="Helvetica-Bold",
        leading=20, spaceBefore=14, spaceAfter=6)
H2 = S("H2", fontSize=13, textColor=DARK_BLUE, fontName="Helvetica-Bold",
        leading=16, spaceBefore=10, spaceAfter=4)
H3 = S("H3", fontSize=11, textColor=MED_BLUE, fontName="Helvetica-Bold",
        leading=14, spaceBefore=8, spaceAfter=3)

BODY = S("Body", fontSize=9.5, textColor=GREY, fontName="Helvetica",
         leading=14, spaceAfter=4, alignment=TA_JUSTIFY)
BULLET = S("Bullet", fontSize=9.5, textColor=GREY, fontName="Helvetica",
           leading=13, spaceAfter=3, leftIndent=14, bulletIndent=4)
FORMULA = S("Formula", fontSize=10, textColor=DARK_BLUE, fontName="Helvetica-Bold",
            leading=14, spaceAfter=4, backColor=LIGHT_BLUE,
            borderPad=6, leftIndent=10)
CODE = S("Code", fontSize=8.5, textColor=colors.HexColor("#1a1a1a"),
         fontName="Courier", leading=12, spaceAfter=3,
         backColor=colors.HexColor("#f0f0f0"), leftIndent=12, borderPad=5)
NOTE = S("Note", fontSize=9, textColor=GREEN, fontName="Helvetica-BoldOblique",
         leading=12, spaceAfter=3)
WARN = S("Warn", fontSize=9, textColor=ORANGE, fontName="Helvetica-BoldOblique",
         leading=12, spaceAfter=3)
MCQ  = S("MCQ",  fontSize=9.5, textColor=GREY, fontName="Helvetica", leading=13, spaceAfter=2)
ANS  = S("Ans",  fontSize=9.5, textColor=GREEN, fontName="Helvetica-Bold", leading=13)
STEP = S("Step", fontSize=9.5, textColor=DARK_BLUE, fontName="Helvetica-Bold",
         leading=13, spaceAfter=2, leftIndent=10)

# ── helper flowables ──────────────────────────────────────────────────────────
class ColorBox(Flowable):
    """Coloured background box for section headers."""
    def __init__(self, width, height, fill_color, radius=4):
        Flowable.__init__(self)
        self.bw, self.bh = width, height
        self.fill = fill_color
        self.radius = radius
    def draw(self):
        self.canv.setFillColor(self.fill)
        self.canv.roundRect(0, 0, self.bw, self.bh, self.radius, fill=1, stroke=0)

def section_header(text, bg=DARK_BLUE, sub=None):
    """Return a list of flowables forming a coloured section header."""
    items = [Spacer(1, 10)]
    w = W - 4*cm
    box = ColorBox(w, 32 if sub else 26, bg, radius=5)
    p   = Paragraph(text, H1)
    tbl = Table([[box, ""]], colWidths=[w, 0])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("ROUNDEDCORNERS", [5]),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 12),
    ]))
    # simpler: just a coloured table
    tdata = [[Paragraph(text, H1)]]
    if sub:
        tdata.append([Paragraph(sub, S("sub_in_hdr", fontSize=9,
            textColor=colors.HexColor("#b3e5fc"), fontName="Helvetica"))])
    th = Table(tdata, colWidths=[w])
    th.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), bg),
        ("ROUNDEDCORNERS",[5]),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
    ]))
    items.append(th)
    items.append(Spacer(1,6))
    return items

def sub_header(text, color=ACCENT):
    tbl = Table([[Paragraph(text, H2)]], colWidths=[W-4*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), LIGHT_BLUE),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LINEBELOW",     (0,0), (-1,-1), 2, ACCENT),
    ]))
    return [Spacer(1,6), tbl, Spacer(1,4)]

def info_box(text, bg=ACCENT_LIGHT, border=ACCENT):
    tbl = Table([[Paragraph(text, BODY)]], colWidths=[W-4*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), bg),
        ("LINERIGHT",     (0,0), (0,-1), 4, border),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 12),
    ]))
    return [tbl, Spacer(1,4)]

def code_block(lines):
    items = []
    for ln in lines:
        items.append(Paragraph(ln, CODE))
    tbl = Table([[Paragraph("<br/>".join(lines), CODE)]], colWidths=[W-4*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#f0f4f8")),
        ("LINERIGHT",     (0,0), (0,-1), 4, ACCENT),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
    ]))
    return [tbl, Spacer(1,4)]

def formula_box(text):
    tbl = Table([[Paragraph(text, FORMULA)]], colWidths=[W-4*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), LIGHT_BLUE),
        ("BOX",           (0,0), (-1,-1), 1.5, DARK_BLUE),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 12),
    ]))
    return [tbl, Spacer(1,4)]

def make_table(headers, rows, col_widths=None, header_bg=DARK_BLUE):
    data = [[Paragraph(f"<b>{h}</b>", S("th", fontSize=9, textColor=WHITE,
            fontName="Helvetica-Bold", leading=12)) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), S("td", fontSize=9, textColor=GREY,
                    fontName="Helvetica", leading=12)) for c in row])
    if col_widths is None:
        cw = (W - 4*cm) / len(headers)
        col_widths = [cw]*len(headers)
    tbl = Table(data, colWidths=col_widths, repeatRows=1)
    style = [
        ("BACKGROUND",    (0,0), (-1,0),  header_bg),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [WHITE, LIGHT_GREY]),
        ("GRID",          (0,0), (-1,-1), 0.5, colors.HexColor("#bdbdbd")),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("ALIGN",         (0,0), (-1,-1), "LEFT"),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
    ]
    tbl.setStyle(TableStyle(style))
    return [tbl, Spacer(1,6)]

def bp(text):
    return Paragraph(f"&#8226; {text}", BULLET)

def p(text):
    return Paragraph(text, BODY)

def h3(text):
    return Paragraph(text, H3)

def sp(n=6):
    return Spacer(1, n)

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#bdbdbd"), spaceAfter=4)

# ═══════════════════════════════════════════════════════════════════════════════
# BUILD DOCUMENT
# ═══════════════════════════════════════════════════════════════════════════════
story = []

# ── COVER PAGE ─────────────────────────────────────────────────────────────────
cover_data = [[
    Paragraph("DATA SCIENCE &amp; MACHINE LEARNING", COVER_SUB),
    Paragraph("UNIT III", COVER_TITLE),
    Paragraph("Data Handling, Wrangling &amp; Preprocessing", COVER_TITLE),
    Spacer(1,12),
    Paragraph("Complete Topper-Level Exam Notes", COVER_TAG),
    Spacer(1,20),
    Paragraph("&#10003; All Syllabus Topics Covered  &#10003; 8+ Numerical Problems  "
              "&#10003; 30+ MCQs  &#10003; Workflows &amp; Diagrams  "
              "&#10003; Comparison Tables  &#10003; Case Studies", COVER_SUB),
]]
cover = Table(cover_data, colWidths=[W-4*cm])
cover.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), DARK_BLUE),
    ("TOPPADDING",    (0,0), (-1,-1), 40),
    ("BOTTOMPADDING", (0,0), (-1,-1), 40),
    ("LEFTPADDING",   (0,0), (-1,-1), 30),
    ("RIGHTPADDING",  (0,0), (-1,-1), 30),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
]))
story.append(cover)
story.append(PageBreak())

# ── TABLE OF CONTENTS ──────────────────────────────────────────────────────────
story += section_header("📋 TABLE OF CONTENTS", DARK_BLUE)
toc_items = [
    ("1", "Data Importing & Exporting",           "3"),
    ("2", "Handling Missing Values",               "5"),
    ("3", "Outlier Detection & Treatment",         "8"),
    ("4", "Data Transformation",                   "11"),
    ("5", "Categorical Encoding",                  "13"),
    ("6", "Data Cleaning Workflow",                "15"),
    ("7", "Data Integration",                      "17"),
    ("8", "Preparing Data for Analysis",           "18"),
    ("9", "Preprocessing Pipelines",               "20"),
    ("10","Advanced Data Operations",              "21"),
    ("11","Numerical Problems (8 Solved)",         "24"),
    ("12","Comparison Tables",                     "29"),
    ("13","Real-World Case Studies",               "31"),
    ("14","MCQ Bank (30 Questions)",               "33"),
    ("15","Short & Long Answer Questions",         "36"),
    ("16","Memory Tricks & Quick Revision",        "38"),
]
story += make_table(["No.", "Topic", "Page"],
    toc_items, col_widths=[1.2*cm, 12.5*cm, 1.5*cm])
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1 – DATA IMPORTING & EXPORTING
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("📥 SECTION 1: Data Importing & Exporting", DARK_BLUE)
story.append(p("<b>Definition:</b> Data importing is the process of reading data from external sources "
               "(files, databases, APIs) into a Python environment for analysis. Exporting is writing "
               "processed data back to storage."))
story.append(p("<b>Why it matters:</b> Raw data rarely lives inside Python. Before any preprocessing "
               "can begin, data must be loaded into a DataFrame. Choosing the right import method "
               "prevents encoding errors, type mismatches, and memory issues."))

story += sub_header("1.1 Reading CSV Files")
story += info_box("CSV (Comma-Separated Values) is the most common data format. Each row is a record; "
                  "columns are separated by commas (or other delimiters).", ACCENT_LIGHT, ACCENT)
story += code_block([
    "import pandas as pd",
    "",
    "# Basic read",
    "df = pd.read_csv('data.csv')",
    "",
    "# Advanced options",
    "df = pd.read_csv('data.csv',",
    "    sep=',',          # delimiter",
    "    header=0,         # row index for column names",
    "    index_col='ID',   # use ID column as index",
    "    na_values=['NA','?','--'],  # treat these as NaN",
    "    dtype={'Age': int, 'Salary': float},",
    "    encoding='utf-8',",
    "    skiprows=1,       # skip first row",
    "    nrows=1000        # read only 1000 rows",
    ")",
    "",
    "# Writing CSV",
    "df.to_csv('output.csv', index=False)",
])

story += sub_header("1.2 Reading Excel Files")
story += code_block([
    "# Reading Excel",
    "df = pd.read_excel('data.xlsx', sheet_name='Sheet1')",
    "",
    "# Read all sheets into a dict",
    "all_sheets = pd.read_excel('data.xlsx', sheet_name=None)",
    "",
    "# Writing Excel",
    "df.to_excel('output.xlsx', sheet_name='Cleaned', index=False)",
    "",
    "# Multiple sheets in one file",
    "with pd.ExcelWriter('multi.xlsx') as writer:",
    "    df1.to_excel(writer, sheet_name='Train')",
    "    df2.to_excel(writer, sheet_name='Test')",
])

story += sub_header("1.3 Reading JSON Files")
story += code_block([
    "import json, pandas as pd",
    "",
    "# Method 1: pandas direct",
    "df = pd.read_json('data.json')",
    "",
    "# Method 2: nested JSON",
    "with open('data.json') as f:",
    "    raw = json.load(f)",
    "df = pd.json_normalize(raw['records'])  # flatten nested keys",
    "",
    "# Writing JSON",
    "df.to_json('output.json', orient='records', indent=2)",
])

story += sub_header("1.4 Quick Reference Table")
story += make_table(
    ["Format","Read Function","Write Function","Common Use Case"],
    [
        ["CSV",   "pd.read_csv()",    "df.to_csv()",    "Tabular data, logs"],
        ["Excel", "pd.read_excel()", "df.to_excel()",  "Business reports"],
        ["JSON",  "pd.read_json()",  "df.to_json()",   "Web APIs, configs"],
        ["SQL",   "pd.read_sql()",   "df.to_sql()",    "Databases"],
        ["Parquet","pd.read_parquet()","df.to_parquet()","Big data, fast I/O"],
        ["HTML",  "pd.read_html()",  "df.to_html()",   "Web scraping"],
    ]
)

story += sub_header("1.5 Common Pitfalls")
for txt in [
    "<b>Encoding errors:</b> Use encoding='utf-8' or encoding='latin-1' if you see UnicodeDecodeError.",
    "<b>Date parsing:</b> Use parse_dates=['date_col'] in read_csv() to auto-convert date strings.",
    "<b>Mixed types:</b> Specifying dtype= prevents pandas from guessing wrong column types.",
    "<b>Large files:</b> Use chunksize=10000 to read in chunks and avoid MemoryError.",
]:
    story.append(bp(txt))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2 – HANDLING MISSING VALUES
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("❓ SECTION 2: Handling Missing Values", MED_BLUE)
story.append(p("<b>Definition:</b> Missing values (NaN, None, null) are absent data points in a dataset. "
               "They arise from data collection errors, system failures, or deliberate non-responses."))
story.append(p("<b>Impact:</b> Most ML algorithms cannot handle NaN directly. Improper handling biases "
               "model training and degrades accuracy."))

story += sub_header("2.1 Types of Missing Data")
story += make_table(
    ["Type","Full Name","Description","Example"],
    [
        ["MCAR","Missing Completely At Random",
         "Missingness is unrelated to any data — purely random.",
         "Scale breaks randomly; weight missing for random patients."],
        ["MAR","Missing At Random",
         "Missingness depends on observed data, not the missing value itself.",
         "Older patients less likely to fill in digital forms."],
        ["MNAR","Missing Not At Random",
         "Missingness is related to the missing value — systematic bias.",
         "High-earners skip income field; sick patients miss follow-up."],
    ],
    col_widths=[1.5*cm, 4*cm, 5.5*cm, 4.5*cm]
)

story += sub_header("2.2 Detecting Missing Values")
story += code_block([
    "df.isnull().sum()          # count NaN per column",
    "df.isnull().mean() * 100   # % missing per column",
    "df.info()                  # dtypes + non-null counts",
    "",
    "# Heatmap of missing values (requires seaborn)",
    "import seaborn as sns",
    "sns.heatmap(df.isnull(), cbar=False, cmap='viridis')",
])

story += sub_header("2.3 Deletion Methods")
story.append(h3("A. Row Deletion (Listwise Deletion)"))
story.append(p("Remove entire rows containing missing values."))
story += code_block([
    "df.dropna()                    # drop rows with ANY NaN",
    "df.dropna(how='all')           # drop rows where ALL values are NaN",
    "df.dropna(subset=['Age','Salary'])  # drop only if these cols are NaN",
    "df.dropna(thresh=4)            # keep rows with at least 4 non-NaN values",
])
story += info_box("✅ Use when: MCAR, small % of missing data (&lt;5%), large dataset.<br/>"
                  "❌ Avoid when: MNAR (introduces bias), small dataset (loses too much data).",
                  GREEN_LIGHT, GREEN)

story.append(h3("B. Column Deletion"))
story.append(p("Remove entire features (columns) with excessive missing data."))
story += code_block([
    "# Drop columns with >40% missing values",
    "threshold = 0.4",
    "df.dropna(axis=1, thresh=int(threshold * len(df)))",
    "",
    "# Or explicitly",
    "df.drop(columns=['low_quality_col'], inplace=True)",
])
story += info_box("✅ Use when: Column has >40–60% missing, feature is not critical.<br/>"
                  "❌ Avoid when: Feature is important for prediction.",
                  ORANGE_LIGHT, ORANGE)

story += sub_header("2.4 Imputation Methods")
story.append(h3("A. Mean Imputation"))
story += code_block([
    "df['Salary'].fillna(df['Salary'].mean(), inplace=True)",
    "",
    "# Using sklearn",
    "from sklearn.impute import SimpleImputer",
    "imp = SimpleImputer(strategy='mean')",
    "df[['Salary']] = imp.fit_transform(df[['Salary']])",
])
story += info_box("✅ Use for: Numeric, normally distributed columns with MCAR data.<br/>"
                  "❌ Avoid for: Skewed distributions (use median) or categorical data.", ACCENT_LIGHT, ACCENT)

story.append(h3("B. Median Imputation"))
story += code_block([
    "df['Age'].fillna(df['Age'].median(), inplace=True)",
    "# OR sklearn: strategy='median'",
])
story += info_box("✅ Use for: Numeric columns with outliers or skewed distributions.<br/>"
                  "Median is robust to outliers unlike mean.", GREEN_LIGHT, GREEN)

story.append(h3("C. Mode Imputation"))
story += code_block([
    "df['City'].fillna(df['City'].mode()[0], inplace=True)",
    "# OR sklearn: strategy='most_frequent'",
])
story += info_box("✅ Use for: Categorical columns.<br/>"
                  "❌ Avoid for: Numerical data with continuous distribution.", ACCENT_LIGHT, ACCENT)

story.append(h3("D. Forward Fill / Backward Fill"))
story += code_block([
    "# Forward fill: use last valid value",
    "df['StockPrice'].fillna(method='ffill', inplace=True)",
    "",
    "# Backward fill: use next valid value",
    "df['StockPrice'].fillna(method='bfill', inplace=True)",
])
story += info_box("✅ Use for: Time-series data where values change gradually.<br/>"
                  "Example: stock prices, sensor readings, temperature logs.", ORANGE_LIGHT, ORANGE)

story += sub_header("2.5 When to Use Which Method")
story += make_table(
    ["Situation","Recommended Method","Reason"],
    [
        ["Normal distribution, numeric","Mean imputation","Preserves central tendency"],
        ["Skewed / outliers present","Median imputation","Robust to extremes"],
        ["Categorical variable","Mode imputation","Most frequent is best guess"],
        ["Time-series data","Forward/Backward fill","Temporal continuity"],
        ["MCAR + small %","Row deletion","Simple, unbiased"],
        ["Column > 50% missing","Column deletion","Feature unreliable"],
        ["Complex patterns","KNN / MICE imputation","Uses relationships between features"],
    ]
)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3 – OUTLIER DETECTION & TREATMENT
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("📊 SECTION 3: Outlier Detection & Treatment", colors.HexColor("#4a148c"))
story.append(p("<b>Definition:</b> Outliers are data points that differ significantly from the majority "
               "of observations. They can be errors (measurement noise) or genuine extreme values."))
story.append(p("<b>Impact of outliers:</b> Skew mean/standard deviation, distort regression lines, "
               "mislead clustering, and degrade ML model performance."))

story += sub_header("3.1 IQR (Interquartile Range) Method")
story.append(p("The IQR method is based on the spread of the middle 50% of data. It is "
               "<b>robust to extreme values</b> and works well for skewed distributions."))
story += formula_box(
    "IQR = Q3 - Q1<br/>"
    "Lower Fence = Q1 - 1.5 × IQR<br/>"
    "Upper Fence = Q3 + 1.5 × IQR<br/>"
    "Outlier: any value &lt; Lower Fence  OR  &gt; Upper Fence"
)

story.append(h3("IQR Boxplot — Visual Explanation"))
story.append(p("A boxplot visually encodes the IQR method:"))
for line in [
    "The <b>box</b> spans from Q1 (25th percentile) to Q3 (75th percentile).",
    "The <b>line inside the box</b> is the Median (Q2, 50th percentile).",
    "The <b>whiskers</b> extend to the farthest data point within 1.5×IQR of the box edges.",
    "Any point <b>beyond the whiskers</b> is plotted individually — these are outliers.",
    "Symmetric box → roughly normal distribution. Asymmetric → skewed.",
]:
    story.append(bp(line))

# ASCII-art style boxplot description as a styled table
boxplot_art = [
    ["Outlier ●      |-----[=====|=====]-----|       ● Outlier"],
    ["               Q1    Q1   Med  Q3    Q3+1.5×IQR"],
    ["               -1.5  (box start) Q2 (box end)"],
]
box_tbl = Table(boxplot_art, colWidths=[W-4*cm])
box_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#e8eaf6")),
    ("FONTNAME",      (0,0), (-1,-1), "Courier"),
    ("FONTSIZE",      (0,0), (-1,-1), 9),
    ("TEXTCOLOR",     (0,0), (-1,-1), DARK_BLUE),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("TOPPADDING",    (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("BOX",           (0,0), (-1,-1), 1, DARK_BLUE),
]))
story.append(box_tbl)
story.append(sp(6))

story += sub_header("3.2 IQR Step-by-Step Worked Example")
story.append(p("<b>Dataset (Salaries in ₹1000):</b> 25, 30, 28, 35, 40, 38, 120, 32, 29, 27"))
step_data = [
    ["Step 1","Sort data","25, 27, 28, 29, 30, 32, 35, 38, 40, 120"],
    ["Step 2","Find Q1 (25th pct)","Q1 = average of 3rd & 4th values = (28+29)/2 = 28.5"],
    ["Step 3","Find Q3 (75th pct)","Q3 = average of 7th & 8th values = (35+38)/2 = 36.5"],
    ["Step 4","Calculate IQR","IQR = 36.5 - 28.5 = 8.0"],
    ["Step 5","Lower Fence","28.5 - 1.5×8.0 = 28.5 - 12.0 = 16.5"],
    ["Step 6","Upper Fence","36.5 + 1.5×8.0 = 36.5 + 12.0 = 48.5"],
    ["Step 7","Identify outliers","120 > 48.5  →  120 is an OUTLIER ✓"],
]
story += make_table(["Step","Action","Calculation"], step_data,
                    col_widths=[1.8*cm, 4*cm, 9.7*cm])

story += code_block([
    "import numpy as np",
    "",
    "data = [25,30,28,35,40,38,120,32,29,27]",
    "Q1 = np.percentile(data, 25)   # 28.5",
    "Q3 = np.percentile(data, 75)   # 36.5",
    "IQR = Q3 - Q1                  # 8.0",
    "lower = Q1 - 1.5*IQR           # 16.5",
    "upper = Q3 + 1.5*IQR           # 48.5",
    "outliers = [x for x in data if x < lower or x > upper]",
    "print(outliers)   # [120]",
])

story += sub_header("3.3 Z-Score Method")
story.append(p("The Z-score measures how many standard deviations a data point is from the mean. "
               "Works best when data is <b>approximately normally distributed</b>."))
story += formula_box(
    "Z = (X - μ) / σ<br/>"
    "Where: X = data point,  μ = mean,  σ = standard deviation<br/>"
    "Rule: |Z| &gt; 3  →  Outlier  (99.7% of normal data falls within ±3σ)"
)

story += sub_header("3.4 Z-Score Step-by-Step Worked Example")
story.append(p("<b>Dataset:</b> 10, 12, 14, 13, 11, 100, 12, 13, 11, 14"))
step_data2 = [
    ["Step 1","Calculate Mean","μ = (10+12+14+13+11+100+12+13+11+14)/10 = 210/10 = 21.0"],
    ["Step 2","Calculate Std Dev","σ = √[Σ(Xi-μ)²/n] ≈ 26.87"],
    ["Step 3","Z-score for 100","Z = (100 - 21) / 26.87 = 79/26.87 ≈ 2.94"],
    ["Step 4","Z-score for 10","Z = (10 - 21) / 26.87 = -11/26.87 ≈ -0.41"],
    ["Step 5","Apply threshold","|Z| > 3  →  100 has Z≈2.94 (borderline), check dataset context"],
]
story += make_table(["Step","Action","Calculation"], step_data2,
                    col_widths=[1.8*cm, 4*cm, 9.7*cm])

story += code_block([
    "from scipy import stats",
    "import numpy as np",
    "",
    "data = np.array([10,12,14,13,11,100,12,13,11,14])",
    "z_scores = np.abs(stats.zscore(data))",
    "outliers = data[z_scores > 3]",
    "clean = data[z_scores <= 3]",
    "print('Outliers:', outliers)",
])

story += sub_header("3.5 Outlier Treatment Strategies")
story += make_table(
    ["Strategy","Description","Use When"],
    [
        ["Remove","Delete outlier rows","Error/noise confirmed; large dataset"],
        ["Cap/Winsorize","Replace with boundary value (e.g. Q3+1.5×IQR)","Valid extreme values; preserve row count"],
        ["Log Transform","Apply log(x) to compress range","Right-skewed data (income, population)"],
        ["Treat separately","Build separate model for outliers","Domain knowledge shows different regime"],
        ["Impute","Replace with mean/median","Small dataset, cannot lose rows"],
    ]
)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4 – DATA TRANSFORMATION
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("🔄 SECTION 4: Data Transformation", colors.HexColor("#1b5e20"))
story.append(p("Data transformation converts raw features into a scale/form suitable for ML algorithms. "
               "The two key techniques are <b>Normalization</b> and <b>Standardization</b>."))

story += sub_header("4.1 Normalization (Min-Max Scaling)")
story += formula_box(
    "X_norm = (X - X_min) / (X_max - X_min)<br/>"
    "Output range: [0, 1]   (or [a, b] for custom range)"
)
story.append(p("<b>What it does:</b> Scales all values proportionally into [0,1]. Preserves the "
               "relative distances between points but compresses extreme values."))
story += code_block([
    "from sklearn.preprocessing import MinMaxScaler",
    "",
    "scaler = MinMaxScaler()          # default: [0,1]",
    "df[['Age','Salary']] = scaler.fit_transform(df[['Age','Salary']])",
    "",
    "# Custom range [0, 100]",
    "scaler = MinMaxScaler(feature_range=(0,100))",
])
story += info_box("✅ Best for: Neural networks, KNN, image pixel data (fixed range required).<br/>"
                  "❌ Avoid: When outliers are present (they compress all other values).",
                  GREEN_LIGHT, GREEN)

story += sub_header("4.2 Standardization (Z-Score Scaling)")
story += formula_box(
    "X_std = (X - μ) / σ<br/>"
    "Output: mean=0, std=1  (no fixed range — can be negative or &gt;1)"
)
story.append(p("<b>What it does:</b> Centers data around 0 with unit variance. Values now represent "
               "'how many standard deviations from the mean'."))
story += code_block([
    "from sklearn.preprocessing import StandardScaler",
    "",
    "scaler = StandardScaler()",
    "df[['Age','Salary']] = scaler.fit_transform(df[['Age','Salary']])",
    "",
    "# Always fit on TRAIN, transform BOTH train and test",
    "scaler.fit(X_train)",
    "X_train_scaled = scaler.transform(X_train)",
    "X_test_scaled  = scaler.transform(X_test)   # use same scaler!",
])
story += info_box("✅ Best for: Linear regression, logistic regression, SVM, PCA.<br/>"
                  "✅ Robust when: Data has outliers or unknown distribution.<br/>"
                  "❌ Avoid: When features must stay in a specific range.", ACCENT_LIGHT, ACCENT)

story += sub_header("4.3 Normalization vs Standardization — Key Comparison")
story += make_table(
    ["Criterion","Normalization (Min-Max)","Standardization (Z-Score)"],
    [
        ["Formula","(X-Xmin)/(Xmax-Xmin)","(X-μ)/σ"],
        ["Output Range","[0, 1] (bounded)","Unbounded (can be negative)"],
        ["Effect of Outliers","Severely affected","Mildly affected"],
        ["Preserves distribution","Yes (shape unchanged)","Yes (shape unchanged)"],
        ["Assumes normal dist?","No","No (but works better with it)"],
        ["Use case","KNN, Neural Networks, image data","Linear/logistic regression, SVM, PCA"],
        ["When outliers present","❌ Avoid","✅ Preferred"],
    ]
)

story += sub_header("4.4 Visual Intuition: Effect on Distribution")
visual_desc = (
    "BEFORE SCALING:  Ages [18, 25, 30, 45, 60]  —  range = 42 units<br/>"
    "AFTER Min-Max:   [0.0, 0.167, 0.286, 0.643, 1.0]  —  range = [0,1]<br/>"
    "AFTER Z-Score:   [-1.29, -0.77, -0.41, 0.52, 1.95]  —  mean=0, std=1<br/><br/>"
    "Key insight: Both methods change the SCALE but NOT the shape of the distribution."
)
story += info_box(visual_desc, YELLOW_LIGHT, ORANGE)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 5 – CATEGORICAL ENCODING
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("🏷️ SECTION 5: Categorical Encoding", colors.HexColor("#bf360c"))
story.append(p("ML algorithms work with numbers, not strings. Categorical encoding converts text "
               "categories into numerical representations that algorithms can process."))

story += sub_header("5.1 Label Encoding")
story.append(p("Assigns a unique integer to each category. Simple, but implies an artificial ordinal "
               "relationship (e.g., Red=0 &lt; Green=1 &lt; Blue=2)."))
story += code_block([
    "from sklearn.preprocessing import LabelEncoder",
    "",
    "le = LabelEncoder()",
    "df['Color_encoded'] = le.fit_transform(df['Color'])",
    "",
    "# Before: ['Red','Green','Blue','Red','Green']",
    "# After:  [  2,     1,     0,    2,     1   ]",
    "# Classes: Blue=0, Green=1, Red=2 (alphabetical)",
    "",
    "# Decode back",
    "le.inverse_transform([0, 1, 2])   # ['Blue','Green','Red']",
])
story += info_box("✅ Use for: <b>Ordinal data</b> (Low/Medium/High) or tree-based models "
                  "(Decision Trees, Random Forest, XGBoost) — these handle arbitrary integers well.<br/>"
                  "❌ Avoid for: Linear models with nominal data — implies false ordering.",
                  ORANGE_LIGHT, ORANGE)

story += sub_header("5.2 One-Hot Encoding (OHE)")
story.append(p("Creates a new binary column for each category. No ordinal relationship is implied. "
               "Also called <b>dummy encoding</b>."))
story += code_block([
    "# pandas get_dummies",
    "df = pd.get_dummies(df, columns=['Color'], drop_first=True)",
    "",
    "# Before: Color = ['Red','Green','Blue']",
    "# After adds: Color_Green=0/1, Color_Red=0/1",
    "# (Blue is the reference category — drop_first removes it)",
    "",
    "# sklearn OneHotEncoder",
    "from sklearn.preprocessing import OneHotEncoder",
    "ohe = OneHotEncoder(drop='first', sparse=False)",
    "encoded = ohe.fit_transform(df[['Color']])",
])
story += info_box("✅ Use for: Nominal categorical data with linear models, neural networks.<br/>"
                  "❌ Avoid for: High-cardinality columns (e.g., 1000 cities → 1000 new columns).",
                  GREEN_LIGHT, GREEN)

story += sub_header("5.3 Dummy Variable Trap")
story.append(p("The dummy variable trap occurs when one dummy variable can be predicted from the others "
               "(perfect multicollinearity). This breaks linear regression."))
story += info_box(
    "<b>Example:</b> Color has 3 categories: Red, Green, Blue.<br/>"
    "If Color_Red=0 and Color_Green=0, we KNOW it is Blue — so Blue column is redundant.<br/>"
    "<b>Fix:</b> Use drop_first=True in get_dummies() to drop one category (reference category).",
    RED_LIGHT, RED
)

story += sub_header("5.4 Label vs One-Hot Encoding Comparison")
story += make_table(
    ["Criterion","Label Encoding","One-Hot Encoding"],
    [
        ["Output","Single integer column","N-1 binary columns"],
        ["Implies order","Yes (may mislead model)","No"],
        ["Memory use","Low","High (many columns)"],
        ["Best for","Ordinal data, tree models","Nominal data, linear models"],
        ["High cardinality","OK","Creates too many columns"],
        ["Example","Low=0, Med=1, High=2","[is_Green, is_Red] per row"],
    ]
)

story += sub_header("5.5 Other Encoding Methods (Advanced)")
story += make_table(
    ["Method","Description","Use Case"],
    [
        ["Ordinal Encoding","Manual integer mapping respecting order","Education: HS=1, BSc=2, MSc=3"],
        ["Binary Encoding","Convert integer to binary bits","High cardinality, saves columns"],
        ["Target Encoding","Replace category with mean of target","Kaggle competitions, tree models"],
        ["Frequency Encoding","Replace with category frequency","Large cardinality columns"],
    ]
)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 6 – DATA CLEANING WORKFLOW
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("🧹 SECTION 6: Data Cleaning Workflow", colors.HexColor("#006064"))

story.append(p("Data cleaning (also called data scrubbing) is the process of detecting and correcting "
               "corrupt, inaccurate, incomplete, or irrelevant data. It is estimated that data scientists "
               "spend <b>60–80% of their time</b> cleaning data."))

story += sub_header("6.1 Step-by-Step Data Cleaning Pipeline")
steps = [
    ("Step 1", "Load & Inspect",
     "df.head(), df.info(), df.describe(), df.shape — understand structure, dtypes, ranges."),
    ("Step 2", "Identify Missing Values",
     "df.isnull().sum() — quantify NaN per column; decide deletion vs imputation."),
    ("Step 3", "Handle Missing Values",
     "Apply mean/median/mode/fill as appropriate (see Section 2)."),
    ("Step 4", "Detect & Remove Duplicates",
     "df.duplicated().sum(); df.drop_duplicates(inplace=True)."),
    ("Step 5", "Fix Data Types",
     "df['date'] = pd.to_datetime(df['date']); df['age'] = df['age'].astype(int)."),
    ("Step 6", "Standardize Text",
     "df['City'] = df['City'].str.strip().str.lower() — removes spaces and case inconsistency."),
    ("Step 7", "Detect & Treat Outliers",
     "Apply IQR or Z-score method (see Section 3). Remove, cap, or transform."),
    ("Step 8", "Fix Inconsistencies",
     "Replace typos: df['Gender'].replace({'M':'Male','F':'Female'}, inplace=True)."),
    ("Step 9", "Validate & Document",
     "Re-run df.info() and df.describe() to verify. Log all changes made."),
]
pipeline_data = [[Paragraph(f"<b>{s[0]}</b>", STEP),
                  Paragraph(f"<b>{s[1]}</b>", H3),
                  Paragraph(s[2], BODY)] for s in steps]
ptbl = Table(pipeline_data, colWidths=[1.8*cm, 3.5*cm, 10.2*cm])
ptbl.setStyle(TableStyle([
    ("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT_BLUE, WHITE]),
    ("GRID",         (0,0),(-1,-1), 0.4, colors.HexColor("#bdbdbd")),
    ("TOPPADDING",   (0,0),(-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1), 5),
    ("LEFTPADDING",  (0,0),(-1,-1), 6),
    ("VALIGN",       (0,0),(-1,-1), "TOP"),
]))
story.append(ptbl)
story.append(sp(8))

story += sub_header("6.2 Complete Code Example")
story += code_block([
    "import pandas as pd",
    "import numpy as np",
    "",
    "df = pd.read_csv('employees.csv')",
    "",
    "# Step 1: Inspect",
    "print(df.info())",
    "print(df.describe())",
    "",
    "# Step 2-3: Missing values",
    "df['Salary'].fillna(df['Salary'].median(), inplace=True)",
    "df['Department'].fillna(df['Department'].mode()[0], inplace=True)",
    "df.dropna(subset=['EmployeeID'], inplace=True)  # critical key",
    "",
    "# Step 4: Duplicates",
    "df.drop_duplicates(inplace=True)",
    "",
    "# Step 5: Fix types",
    "df['JoinDate'] = pd.to_datetime(df['JoinDate'])",
    "df['Age'] = df['Age'].astype(int)",
    "",
    "# Step 6: Standardize text",
    "df['City'] = df['City'].str.strip().str.title()",
    "df['Gender'] = df['Gender'].str.upper().replace({'M':'Male','F':'Female'})",
    "",
    "# Step 7: Outliers (IQR on Salary)",
    "Q1 = df['Salary'].quantile(0.25)",
    "Q3 = df['Salary'].quantile(0.75)",
    "IQR = Q3 - Q1",
    "df = df[(df['Salary'] >= Q1-1.5*IQR) & (df['Salary'] <= Q3+1.5*IQR)]",
    "",
    "# Step 9: Validate",
    "print(df.isnull().sum())",
    "df.to_csv('employees_clean.csv', index=False)",
])
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 7 – DATA INTEGRATION
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("🔗 SECTION 7: Data Integration", colors.HexColor("#37474f"))
story.append(p("Data integration combines data from multiple sources into a unified view. "
               "Challenges include schema mismatches, naming conflicts, and duplicate records."))

story += sub_header("7.1 Combining Datasets")
story += code_block([
    "# Vertical stacking (same columns, more rows)",
    "combined = pd.concat([df1, df2, df3], ignore_index=True)",
    "",
    "# Horizontal stacking (same rows, more columns)",
    "combined = pd.concat([df_features, df_labels], axis=1)",
])

story += sub_header("7.2 Merging (SQL-Style Joins)")
story += make_table(
    ["Join Type","Description","Result"],
    [
        ["INNER JOIN","Only rows that match in BOTH dataframes","Smallest result"],
        ["LEFT JOIN","All rows from left + matching from right","Left df preserved"],
        ["RIGHT JOIN","All rows from right + matching from left","Right df preserved"],
        ["OUTER JOIN","All rows from both; NaN where no match","Largest result"],
    ]
)
story += code_block([
    "# Inner join on 'CustomerID'",
    "result = pd.merge(orders, customers, on='CustomerID', how='inner')",
    "",
    "# Left join (keep all orders even if customer missing)",
    "result = pd.merge(orders, customers, on='CustomerID', how='left')",
    "",
    "# Join on different column names",
    "result = pd.merge(df1, df2,",
    "    left_on='emp_id', right_on='employee_id', how='inner')",
])

story += sub_header("7.3 Handling Schema Differences & Conflicts")
for txt in [
    "<b>Column name mismatch:</b> Use rename() before merging or left_on/right_on in merge().",
    "<b>Duplicate columns:</b> merge() adds suffixes (_x, _y) automatically — rename as needed.",
    "<b>Type conflicts:</b> Cast both to common type before joining: df['id'] = df['id'].astype(str).",
    "<b>Duplicate records:</b> After merging, run drop_duplicates() to remove artifact duplicates.",
    "<b>Missing keys:</b> Use how='left' or 'outer' to preserve unmatched records.",
]:
    story.append(bp(txt))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 8 – PREPARING DATA FOR ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("📐 SECTION 8: Preparing Data for Analysis", colors.HexColor("#1a237e"))

story += sub_header("8.1 Feature Selection")
story.append(p("Feature selection removes irrelevant or redundant features, reducing dimensionality "
               "and improving model speed and accuracy."))
story += make_table(
    ["Method","Type","Description"],
    [
        ["Correlation Filter","Filter","Remove features with |corr| > 0.9 to target or each other"],
        ["Variance Threshold","Filter","Remove near-zero-variance features (uninformative)"],
        ["Chi-Square Test","Filter","For categorical features vs categorical target"],
        ["RFE (Recursive Feature Elim.)","Wrapper","Iteratively remove least important features"],
        ["Lasso (L1 Regularization)","Embedded","Shrinks unimportant feature weights to 0"],
        ["Feature Importance (Trees)","Embedded","Random Forest / XGBoost importance scores"],
    ]
)
story += code_block([
    "from sklearn.feature_selection import SelectKBest, f_classif",
    "",
    "selector = SelectKBest(score_func=f_classif, k=10)",
    "X_new = selector.fit_transform(X, y)",
    "selected_features = X.columns[selector.get_support()]",
])

story += sub_header("8.2 Feature Scaling")
story.append(p("Already covered in Section 4 (Normalization & Standardization). "
               "Key rule: <b>Always fit the scaler on training data only</b>, then transform both "
               "train and test — prevents data leakage."))

story += sub_header("8.3 Data Formatting")
for txt in [
    "<b>Date features:</b> Extract year, month, day, day-of-week as separate numeric columns.",
    "<b>String cleaning:</b> Strip whitespace, lowercase, remove special characters.",
    "<b>Boolean:</b> Convert True/False to 1/0 with df.astype(int).",
    "<b>Binning:</b> Convert continuous to categorical: pd.cut(df['Age'], bins=[0,18,35,60,100], labels=['Teen','Young','Mid','Senior']).",
]:
    story.append(bp(txt))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 9 – PREPROCESSING PIPELINES
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("⚙️ SECTION 9: Preprocessing Pipelines", colors.HexColor("#004d40"))
story.append(p("A <b>pipeline</b> chains multiple preprocessing steps into a single object. "
               "This ensures the exact same transformations are applied to training and test data, "
               "prevents data leakage, and makes code clean and reproducible."))

story += sub_header("9.1 Why Use Pipelines?")
for txt in [
    "Prevents data leakage: scaler.fit() is only called on training data.",
    "Reproducibility: one pipeline object encapsulates the entire workflow.",
    "Deployment simplicity: save one pipeline object, load it in production.",
    "Cross-validation: GridSearchCV integrates seamlessly with Pipeline.",
]:
    story.append(bp(txt))

story += sub_header("9.2 sklearn Pipeline Example")
story += code_block([
    "from sklearn.pipeline import Pipeline",
    "from sklearn.preprocessing import StandardScaler, OneHotEncoder",
    "from sklearn.impute import SimpleImputer",
    "from sklearn.compose import ColumnTransformer",
    "from sklearn.ensemble import RandomForestClassifier",
    "",
    "# Define column groups",
    "numeric_cols = ['Age', 'Salary', 'Experience']",
    "cat_cols     = ['City', 'Department']",
    "",
    "# Numeric pipeline: impute then scale",
    "num_pipeline = Pipeline([",
    "    ('imputer', SimpleImputer(strategy='median')),",
    "    ('scaler',  StandardScaler())",
    "])",
    "",
    "# Categorical pipeline: impute then encode",
    "cat_pipeline = Pipeline([",
    "    ('imputer', SimpleImputer(strategy='most_frequent')),",
    "    ('encoder', OneHotEncoder(handle_unknown='ignore', drop='first'))",
    "])",
    "",
    "# Combine both",
    "preprocessor = ColumnTransformer([",
    "    ('num', num_pipeline, numeric_cols),",
    "    ('cat', cat_pipeline, cat_cols)",
    "])",
    "",
    "# Full pipeline with model",
    "full_pipeline = Pipeline([",
    "    ('preprocessor', preprocessor),",
    "    ('classifier',   RandomForestClassifier(n_estimators=100))",
    "])",
    "",
    "# Fit and predict",
    "full_pipeline.fit(X_train, y_train)",
    "predictions = full_pipeline.predict(X_test)",
])

story += sub_header("9.3 ML Preprocessing Pipeline — Architecture Diagram")
arch_steps = [
    ["RAW DATA","→","Load (read_csv)","→","Inspect (info, describe)"],
    ["↓","","↓","","↓"],
    ["CLEANING","→","Handle NaN","→","Remove Duplicates"],
    ["↓","","↓","","↓"],
    ["TRANSFORM","→","Encode Categoricals","→","Scale Numerics"],
    ["↓","","↓","","↓"],
    ["FEATURES","→","Feature Selection","→","Train/Test Split"],
    ["↓","","↓","","↓"],
    ["MODEL","→","Fit Pipeline","→","Evaluate & Deploy"],
]
arch_tbl = Table(arch_steps, colWidths=[3*cm]*5)
arch_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (0,-1), DARK_BLUE),
    ("BACKGROUND",    (2,0), (2,-1), ACCENT),
    ("BACKGROUND",    (4,0), (4,-1), colors.HexColor("#1b5e20")),
    ("TEXTCOLOR",     (0,0), (0,-1), WHITE),
    ("TEXTCOLOR",     (2,0), (2,-1), WHITE),
    ("TEXTCOLOR",     (4,0), (4,-1), WHITE),
    ("FONTNAME",      (0,0), (-1,-1), "Helvetica-Bold"),
    ("FONTSIZE",      (0,0), (-1,-1), 8),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("GRID",          (0,0), (-1,-1), 0.5, colors.HexColor("#bdbdbd")),
]))
story.append(arch_tbl)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 10 – ADVANCED DATA OPERATIONS
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("🚀 SECTION 10: Advanced Data Operations", colors.HexColor("#311b92"))

story += sub_header("10.1 Merging DataFrames")
story.append(p("Already introduced in Section 7 (joins). Additional details:"))
story += code_block([
    "# Multi-key join",
    "pd.merge(df1, df2, on=['Year','Quarter'], how='inner')",
    "",
    "# Index-based join",
    "df1.join(df2, how='left')         # joins on index by default",
    "",
    "# Cross join (all combinations)",
    "pd.merge(df1, df2, how='cross')   # pandas 1.2+",
])

story += sub_header("10.2 Reshaping Data")
story.append(h3("Pivot — Long to Wide"))
story += code_block([
    "# pivot_table: aggregate with function",
    "pivot = df.pivot_table(",
    "    values='Sales',",
    "    index='Region',",
    "    columns='Month',",
    "    aggfunc='sum',",
    "    fill_value=0",
    ")",
])
story.append(h3("Melt — Wide to Long"))
story += code_block([
    "# melt: unpivot wide format to long format",
    "long_df = df.melt(",
    "    id_vars=['EmployeeID','Name'],",
    "    value_vars=['Q1_Sales','Q2_Sales','Q3_Sales'],",
    "    var_name='Quarter',",
    "    value_name='Sales'",
    ")",
])

story += sub_header("10.3 Time-Series Wrangling")
story += code_block([
    "# Parse dates",
    "df['date'] = pd.to_datetime(df['date'])",
    "df.set_index('date', inplace=True)",
    "",
    "# Resample (aggregate by time period)",
    "monthly = df['Sales'].resample('M').sum()   # monthly totals",
    "weekly  = df['Sales'].resample('W').mean()  # weekly averages",
    "",
    "# Rolling window",
    "df['7day_MA'] = df['Sales'].rolling(window=7).mean()",
    "",
    "# Lag features",
    "df['Sales_lag1'] = df['Sales'].shift(1)   # previous day's sales",
    "",
    "# Extract time components",
    "df['year']    = df.index.year",
    "df['month']   = df.index.month",
    "df['dayofweek'] = df.index.dayofweek",
])

story += sub_header("10.4 Sampling Techniques")
story += make_table(
    ["Technique","Description","Code / Use Case"],
    [
        ["Random Sampling","Select n rows randomly","df.sample(n=500, random_state=42)"],
        ["Stratified Sampling","Preserve class proportions","train_test_split(X, y, stratify=y)"],
        ["Systematic Sampling","Every k-th row","df.iloc[::k]"],
        ["Oversampling","Increase minority class","SMOTE from imblearn"],
        ["Undersampling","Reduce majority class","RandomUnderSampler from imblearn"],
        ["Bootstrap Sampling","Sample with replacement","df.sample(frac=1.0, replace=True)"],
    ]
)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 11 – NUMERICAL PROBLEMS
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("🔢 SECTION 11: Solved Numerical Problems", colors.HexColor("#880e4f"))

def num_problem(num, title, question, steps, answer, bg=ACCENT_LIGHT):
    items = []
    q_tbl = Table([[Paragraph(f"<b>Problem {num}: {title}</b>", H2)]],
                  colWidths=[W-4*cm])
    q_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), DARK_BLUE),
        ("TOPPADDING",    (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
    ]))
    items.append(q_tbl)
    items.append(sp(4))
    items.append(Paragraph(f"<b>Q:</b> {question}", BODY))
    items.append(sp(3))
    for i, s in enumerate(steps, 1):
        items.append(Paragraph(f"<b>Step {i}:</b> {s}", BULLET))
    items.append(sp(3))
    ans_tbl = Table([[Paragraph(f"✅ <b>Answer:</b> {answer}", ANS)]],
                    colWidths=[W-4*cm])
    ans_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), GREEN_LIGHT),
        ("BOX",        (0,0), (-1,-1), 1.5, GREEN),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1), 6),
        ("LEFTPADDING",(0,0), (-1,-1), 10),
    ]))
    items.append(ans_tbl)
    items.append(sp(10))
    return items

story += num_problem(1, "Mean Imputation",
    "Dataset: Exam scores [78, NaN, 85, 90, NaN, 72, 88]. Replace NaN with the mean.",
    [
        "List non-NaN values: 78, 85, 90, 72, 88",
        "Sum = 78 + 85 + 90 + 72 + 88 = 413",
        "Count of non-NaN = 5",
        "Mean = 413 / 5 = 82.6",
        "Replace NaN: [78, 82.6, 85, 90, 82.6, 72, 88]",
    ],
    "Imputed dataset: [78, 82.6, 85, 90, 82.6, 72, 88]"
)

story += num_problem(2, "Median Imputation",
    "Ages: [22, NaN, 35, 28, 45, NaN, 30, 60]. Replace NaN with median.",
    [
        "Sort non-NaN: 22, 28, 30, 35, 45, 60",
        "n = 6 (even count)",
        "Median = (3rd + 4th) / 2 = (30 + 35) / 2 = 32.5",
        "Replace NaN: [22, 32.5, 35, 28, 45, 32.5, 30, 60]",
    ],
    "Median = 32.5. Imputed dataset: [22, 32.5, 35, 28, 45, 32.5, 30, 60]"
)

story += num_problem(3, "IQR Outlier Detection",
    "Salaries (₹K): [18, 20, 22, 21, 19, 23, 24, 95, 20, 18]. Find outliers using IQR.",
    [
        "Sort: 18, 18, 19, 20, 20, 21, 22, 23, 24, 95",
        "n = 10; Q1 = average of 3rd & 4th = (19+20)/2 = 19.5",
        "Q3 = average of 7th & 8th = (22+23)/2 = 22.5",
        "IQR = 22.5 - 19.5 = 3.0",
        "Lower fence = 19.5 - 1.5×3.0 = 19.5 - 4.5 = 15.0",
        "Upper fence = 22.5 + 1.5×3.0 = 22.5 + 4.5 = 27.0",
        "Check each value: 95 > 27.0 → OUTLIER",
    ],
    "Outlier detected: 95 (₹95K). All others fall within [15, 27]."
)

story += num_problem(4, "Z-Score Outlier Detection",
    "Test scores: [65, 70, 68, 72, 69, 71, 67, 140]. Identify outlier using Z-score (threshold=3).",
    [
        "Mean μ = (65+70+68+72+69+71+67+140)/8 = 622/8 = 77.75",
        "Deviations²: (65-77.75)²=162.56, (70-77.75)²=60.06, (68-77.75)²=95.06, "
        "(72-77.75)²=33.06, (69-77.75)²=76.56, (71-77.75)²=45.56, "
        "(67-77.75)²=115.56, (140-77.75)²=3876.56",
        "Variance = sum/8 = 4465.0/8 = 558.125",
        "σ = √558.125 ≈ 23.62",
        "Z(140) = (140 - 77.75)/23.62 = 62.25/23.62 ≈ 2.64",
        "Z(65)  = (65 - 77.75)/23.62 = -12.75/23.62 ≈ -0.54",
        "No value exceeds |Z|=3, but 140 is clearly anomalous (check with IQR too).",
    ],
    "Z(140) ≈ 2.64 (below threshold of 3 due to small dataset). IQR method recommended here."
)

story += num_problem(5, "Min-Max Normalization",
    "Feature values: [10, 20, 30, 40, 50]. Normalize to [0, 1].",
    [
        "X_min = 10,  X_max = 50",
        "Formula: X_norm = (X - 10) / (50 - 10) = (X - 10) / 40",
        "10: (10-10)/40 = 0/40 = 0.00",
        "20: (20-10)/40 = 10/40 = 0.25",
        "30: (30-10)/40 = 20/40 = 0.50",
        "40: (40-10)/40 = 30/40 = 0.75",
        "50: (50-10)/40 = 40/40 = 1.00",
    ],
    "Normalized: [0.00, 0.25, 0.50, 0.75, 1.00]"
)

story += num_problem(6, "Z-Score Standardization",
    "Values: [2, 4, 4, 4, 5, 5, 7, 9]. Standardize using Z-score.",
    [
        "n = 8",
        "Mean μ = (2+4+4+4+5+5+7+9)/8 = 40/8 = 5.0",
        "Variance = [(2-5)²+(4-5)²+(4-5)²+(4-5)²+(5-5)²+(5-5)²+(7-5)²+(9-5)²]/8",
        "= [9+1+1+1+0+0+4+16]/8 = 32/8 = 4.0",
        "σ = √4.0 = 2.0",
        "Z(2)=(2-5)/2=-1.5; Z(4)=(4-5)/2=-0.5; Z(5)=(5-5)/2=0.0; Z(7)=(7-5)/2=1.0; Z(9)=(9-5)/2=2.0",
    ],
    "Standardized: [-1.5, -0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 2.0]  (mean=0, std=1)"
)

story += num_problem(7, "Label Encoding",
    "Categories: ['Bronze','Silver','Gold','Silver','Bronze','Gold','Gold']. Apply Label Encoding.",
    [
        "Unique categories (sorted alphabetically): Bronze, Gold, Silver",
        "Assign integers: Bronze=0, Gold=1, Silver=2",
        "Encode: Bronze→0, Silver→2, Gold→1, Silver→2, Bronze→0, Gold→1, Gold→1",
    ],
    "Encoded: [0, 2, 1, 2, 0, 1, 1]"
)

story += num_problem(8, "One-Hot Encoding",
    "Color column: ['Red','Green','Blue','Red']. Apply OHE using drop_first=True.",
    [
        "Unique values: Blue, Green, Red",
        "Reference category (dropped): Blue",
        "Create columns: Color_Green, Color_Red",
        "Red  → Color_Green=0, Color_Red=1",
        "Green → Color_Green=1, Color_Red=0",
        "Blue → Color_Green=0, Color_Red=0  (reference)",
        "Red  → Color_Green=0, Color_Red=1",
    ],
    "Matrix: [(0,1),(1,0),(0,0),(0,1)] for (Color_Green, Color_Red)"
)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 12 – COMPARISON TABLES
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("📊 SECTION 12: Comparison Tables", colors.HexColor("#0d47a1"))

story += sub_header("12.1 Normalization vs Standardization")
story += make_table(
    ["Parameter","Normalization","Standardization"],
    [
        ["Also called","Min-Max Scaling","Z-Score Scaling"],
        ["Formula","(X-Xmin)/(Xmax-Xmin)","(X-μ)/σ"],
        ["Output range","[0,1] (bounded)","Unbounded (≈ -3 to +3)"],
        ["Outlier sensitivity","HIGH — outliers distort bounds","LOW — robust to extremes"],
        ["Assumes distribution","None","None (but better with normal)"],
        ["Best algorithms","KNN, Neural Networks, SVM(RBF)","Linear Regression, Logistic, PCA, SVM"],
        ["Speed effect","Faster convergence in NN","Faster convergence in linear models"],
        ["Preserves zeros","No","No"],
        ["sklearn class","MinMaxScaler","StandardScaler"],
    ]
)

story += sub_header("12.2 Label Encoding vs One-Hot Encoding")
story += make_table(
    ["Parameter","Label Encoding","One-Hot Encoding"],
    [
        ["Output","Single int column","N-1 binary columns"],
        ["Ordinal assumption","Yes (implies ranking)","No"],
        ["High cardinality","Efficient","Creates too many columns"],
        ["Dummy variable trap","Not applicable","Yes — use drop_first=True"],
        ["Best for","Ordinal data, tree models","Nominal data, linear/NN models"],
        ["sklearn class","LabelEncoder","OneHotEncoder"],
        ["pandas equivalent","map() or replace()","get_dummies()"],
    ]
)

story += sub_header("12.3 IQR vs Z-Score Outlier Detection")
story += make_table(
    ["Parameter","IQR Method","Z-Score Method"],
    [
        ["Based on","Percentiles (Q1, Q3)","Mean and Standard Deviation"],
        ["Outlier threshold","1.5 × IQR beyond Q1/Q3","|Z| > 2 or 3"],
        ["Sensitivity to outliers","LOW (robust)","HIGH (outliers inflate σ)"],
        ["Best for","Skewed distributions","Normal distributions"],
        ["Small datasets","Works well","Can be misleading"],
        ["Formula","Q1-1.5×IQR, Q3+1.5×IQR","Z=(X-μ)/σ"],
        ["Visual tool","Boxplot","Normal distribution curve"],
    ]
)

story += sub_header("12.4 Deletion vs Imputation for Missing Values")
story += make_table(
    ["Parameter","Deletion","Imputation"],
    [
        ["Data loss","Yes (rows/columns removed)","No (data preserved)"],
        ["Introduces bias","Yes if data is MNAR","Possible if wrong method"],
        ["Best when","MCAR + small % missing","MAR or large % missing"],
        ["Methods","dropna()","mean/median/mode/KNN/MICE"],
        ["Risk","Reduces statistical power","Can distort distribution"],
        ["Code","df.dropna()","df.fillna(df.mean())"],
    ]
)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 13 – CASE STUDIES
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("📋 SECTION 13: Real-World Case Studies", colors.HexColor("#1b5e20"))

story += sub_header("Case Study 1: Handling Missing Values in Medical Dataset")
story.append(p("<b>Context:</b> A hospital dataset has 5000 patients with columns: Age, Blood Pressure, "
               "Cholesterol, Glucose, Diagnosis. Cholesterol has 18% missing; Glucose has 4% missing."))
story += make_table(
    ["Column","% Missing","Type","Decision","Rationale"],
    [
        ["Cholesterol","18%","Numeric","Median imputation","Skewed; median robust"],
        ["Glucose","4%","Numeric","Mean imputation","Normal distribution"],
        ["Blood Pressure","0%","Numeric","No action","Complete"],
        ["Diagnosis","2%","Categorical","Mode imputation","Most common label"],
    ]
)
story += code_block([
    "df['Cholesterol'].fillna(df['Cholesterol'].median(), inplace=True)",
    "df['Glucose'].fillna(df['Glucose'].mean(), inplace=True)",
    "df['Diagnosis'].fillna(df['Diagnosis'].mode()[0], inplace=True)",
    "",
    "# Verify",
    "print(df.isnull().sum())   # Should print 0 for all",
])
story += info_box("<b>Key lesson:</b> In medical data, deleting rows may eliminate rare disease cases. "
                  "Imputation preserves all patient records.", GREEN_LIGHT, GREEN)

story += sub_header("Case Study 2: Outlier Detection in Salary Dataset")
story.append(p("<b>Context:</b> HR dataset with 200 employee salaries (₹ thousands). "
               "Data entry errors caused salaries of 0 and 9999 to appear."))
story += code_block([
    "import pandas as pd, numpy as np",
    "",
    "# Load",
    "df = pd.read_csv('salaries.csv')",
    "print(df['Salary'].describe())",
    "",
    "# IQR method",
    "Q1  = df['Salary'].quantile(0.25)   # e.g. 45",
    "Q3  = df['Salary'].quantile(0.75)   # e.g. 85",
    "IQR = Q3 - Q1                       # 40",
    "low  = Q1 - 1.5*IQR                 # -15 (set floor to 0)",
    "high = Q3 + 1.5*IQR                 # 145",
    "",
    "# Option 1: Remove outliers",
    "df_clean = df[(df['Salary'] >= 0) & (df['Salary'] <= high)]",
    "",
    "# Option 2: Cap (Winsorize)",
    "df['Salary'] = df['Salary'].clip(lower=0, upper=high)",
    "",
    "print(f'Removed {len(df) - len(df_clean)} outlier rows')",
])
story += info_box("<b>Key lesson:</b> Always visualize with a boxplot first. Domain knowledge "
                  "(salary cannot be negative or 9999) helps decide treatment strategy.", ORANGE_LIGHT, ORANGE)

story += sub_header("Case Study 3: Encoding Categorical Data for ML")
story.append(p("<b>Context:</b> E-commerce dataset for churn prediction. Features: City (50 unique), "
               "Plan (Basic/Standard/Premium), Device (Mobile/Desktop/Tablet)."))
story += make_table(
    ["Feature","Unique Values","Encoding Chosen","Reason"],
    [
        ["City","50 cities","Target Encoding","OHE would create 50 columns"],
        ["Plan","Basic/Standard/Premium","Ordinal Encoding (0,1,2)","Clear order exists"],
        ["Device","Mobile/Desktop/Tablet","One-Hot (drop_first=True)","Nominal, only 3 categories"],
    ]
)
story += code_block([
    "# Plan: ordinal",
    "plan_map = {'Basic':0, 'Standard':1, 'Premium':2}",
    "df['Plan'] = df['Plan'].map(plan_map)",
    "",
    "# Device: one-hot",
    "df = pd.get_dummies(df, columns=['Device'], drop_first=True)",
    "",
    "# City: target encoding (mean of target per city)",
    "city_means = df.groupby('City')['Churn'].mean()",
    "df['City_encoded'] = df['City'].map(city_means)",
    "df.drop(columns=['City'], inplace=True)",
])
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 14 – MCQs
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("✅ SECTION 14: MCQ Bank (30 Questions)", colors.HexColor("#4a148c"))

mcqs = [
    ("Which pandas function reads a CSV file?",
     "a) pd.load_csv()  b) pd.read_csv()  c) pd.import_csv()  d) pd.open_csv()", "b"),
    ("What does df.isnull().sum() return?",
     "a) Sum of all values  b) Count of NaN per column  c) Count of zeros  d) Row count", "b"),
    ("MCAR stands for:",
     "a) Missing Columns At Random  b) Missing Completely At Random  "
     "c) Missing Computed At Runtime  d) Multiple Columns Are Removed", "b"),
    ("Which imputation is best for skewed numeric data?",
     "a) Mean  b) Mode  c) Median  d) Forward fill", "c"),
    ("IQR is calculated as:",
     "a) Q2 - Q1  b) Q3 - Q1  c) Q3 - Q2  d) Mean - Median", "b"),
    ("A value is an outlier by IQR if it is:",
     "a) > Q3  b) < Q1  c) Beyond Q1-1.5*IQR or Q3+1.5*IQR  d) Beyond ±2 std devs", "c"),
    ("Z-score formula is:",
     "a) (X-max)/(max-min)  b) (X-μ)/σ  c) (X-min)/σ  d) (X-Q1)/IQR", "b"),
    ("Min-Max Normalization scales data to:",
     "a) Mean=0, Std=1  b) [0, 1]  c) [-1, 1]  d) Unbounded range", "b"),
    ("Standardization (Z-score scaling) produces output with:",
     "a) Range [0,1]  b) All positive values  c) Mean=0, Std=1  d) Max=1", "c"),
    ("Which scaler is more sensitive to outliers?",
     "a) StandardScaler  b) MinMaxScaler  c) RobustScaler  d) All equal", "b"),
    ("Label Encoding assigns:",
     "a) Binary columns per category  b) Integer per category  "
     "c) Float per category  d) Random value", "b"),
    ("The Dummy Variable Trap is solved by:",
     "a) Using all dummy columns  b) Using drop_first=True  "
     "c) Adding more categories  d) Using LabelEncoder", "b"),
    ("One-Hot Encoding is NOT suitable when:",
     "a) Data is categorical  b) Model is linear  "
     "c) Column has 500 unique values  d) Using neural networks", "c"),
    ("Which join keeps only matching rows from both tables?",
     "a) LEFT  b) RIGHT  c) OUTER  d) INNER", "d"),
    ("pd.merge(df1, df2, how='left') keeps:",
     "a) All rows from df2  b) Only matching rows  c) All rows from df1  d) All rows from both", "c"),
    ("Forward fill (ffill) is best used for:",
     "a) Medical records  b) Time-series data  c) Categorical data  d) High-dimensional data", "b"),
    ("df.drop_duplicates() removes:",
     "a) NaN rows  b) Rows with outliers  c) Rows that are exact copies  d) Zero rows", "c"),
    ("Which method is used to detect outliers visually?",
     "a) Histogram  b) Scatter plot  c) Boxplot  d) Pie chart", "c"),
    ("The sklearn class for Min-Max scaling is:",
     "a) Normalizer  b) MinMaxScaler  c) StandardScaler  d) RobustScaler", "b"),
    ("Feature scaling should be fit on:",
     "a) Test data only  b) Entire dataset  c) Training data only  d) Validation data only", "c"),
    ("Which of these is NOT a type of missing data?",
     "a) MCAR  b) MAR  c) MNAR  d) MFAR", "d"),
    ("pd.pivot_table converts data from:",
     "a) Wide to long  b) Long to wide  c) Vertical to horizontal  d) Numeric to categorical", "b"),
    ("pd.melt converts data from:",
     "a) Long to wide  b) Wide to long  c) JSON to CSV  d) Float to int", "b"),
    ("A pipeline in sklearn is used to:",
     "a) Plot data  b) Chain preprocessing + model steps  c) Read CSV  d) Merge datasets", "b"),
    ("Which encoding is appropriate for 'Education Level' (High School, Bachelor, Master, PhD)?",
     "a) One-Hot  b) Binary  c) Ordinal/Label  d) Target", "c"),
    ("RobustScaler uses which statistics?",
     "a) Mean and Std  b) Min and Max  c) Median and IQR  d) Mode and Range", "c"),
    ("What does df.dropna(thresh=3) do?",
     "a) Drop rows with 3 NaN  b) Keep rows with at least 3 non-NaN  "
     "c) Drop columns with 3 NaN  d) Drop rows with more than 3 values", "b"),
    ("Which sampling technique preserves class ratios?",
     "a) Random sampling  b) Systematic sampling  c) Stratified sampling  d) Bootstrap", "c"),
    ("SMOTE is used to handle:",
     "a) Outliers  b) Missing values  c) Imbalanced datasets  d) Encoding issues", "c"),
    ("Data leakage in preprocessing occurs when:",
     "a) Data is deleted  b) Scaler is fit on full dataset including test  "
     "c) Outliers are removed  d) Encoding is wrong", "b"),
]

for i, (q, opts, ans) in enumerate(mcqs, 1):
    story.append(Paragraph(f"<b>Q{i}.</b> {q}", MCQ))
    story.append(Paragraph(opts, S("opts", fontSize=9, textColor=colors.HexColor("#555"),
                                   fontName="Helvetica", leading=12, leftIndent=12)))
    story.append(Paragraph(f"Answer: ({ans})", ANS))
    story.append(sp(3))
    if i % 10 == 0:
        story.append(hr())
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 15 – SHORT & LONG ANSWER QUESTIONS
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("📝 SECTION 15: Short & Long Answer Questions", colors.HexColor("#004d40"))

story += sub_header("Short Answer Questions (2–4 marks)")
shorts = [
    ("Define MCAR, MAR, and MNAR with one example each.",
     "MCAR: Missing Completely At Random — random equipment failure. "
     "MAR: Missing At Random — older people skip digital forms (depends on observed Age). "
     "MNAR: Missing Not At Random — sick patients don't show for follow-up (missing depends on health itself)."),
    ("What is the Dummy Variable Trap? How is it avoided?",
     "When one dummy column is perfectly predictable from others (perfect multicollinearity), "
     "causing issues in linear models. Avoided by using drop_first=True in get_dummies() "
     "or drop='first' in OneHotEncoder."),
    ("Differentiate between normalization and standardization.",
     "Normalization scales to [0,1] using Min-Max formula. "
     "Standardization scales to mean=0, std=1 using Z-score. "
     "Normalization is sensitive to outliers; standardization is more robust."),
    ("Why should you fit a scaler only on training data?",
     "Fitting on test data would leak information about the test distribution into preprocessing, "
     "making evaluation optimistic (data leakage). The test set must remain completely unseen."),
    ("What is forward fill and when is it used?",
     "Forward fill propagates the last valid value forward to fill NaN. "
     "Used for time-series data where values change gradually (stock prices, sensor data, weather)."),
]
for q, a in shorts:
    story.append(Paragraph(f"<b>Q:</b> {q}", H3))
    story.append(Paragraph(f"<b>A:</b> {a}", BODY))
    story.append(sp(4))

story += sub_header("Long Answer Questions (8–10 marks)")
longs = [
    "Explain the complete data cleaning workflow with a real dataset example. "
    "Include all steps from loading to validation with code snippets.",
    "Describe the IQR and Z-score methods for outlier detection. Compare them with a "
    "numerical example showing step-by-step calculations for both methods.",
    "What is a preprocessing pipeline in sklearn? Build a complete pipeline that handles "
    "missing values, encodes categorical data, scales numeric features, and trains a "
    "Random Forest classifier. Explain why pipelines are important.",
    "Explain all types of joins (inner, left, right, outer) in pandas with examples. "
    "When would you use each type? Include code for each.",
    "Compare Label Encoding and One-Hot Encoding. Give examples of when each should be "
    "used and explain the dummy variable trap with a solution.",
]
for i, q in enumerate(longs, 1):
    story.append(Paragraph(f"<b>Long Q{i}:</b> {q}", BODY))
    story.append(sp(5))

story += sub_header("Case-Based Question (10 marks)")
story.append(p("<b>Scenario:</b> You receive a dataset of 10,000 customer records with columns: "
               "CustomerID, Age (15% missing), Income (30% missing, right-skewed), "
               "City (50 unique values), Plan (Basic/Standard/Premium), "
               "Churn (0/1, 80% zeros — imbalanced), LastLogin (date string)."))
story.append(p("<b>Tasks:</b>"))
tasks = [
    "How will you handle the missing Age and Income values? Justify your choice.",
    "Which encoding will you apply to City and Plan? Why?",
    "LastLogin is a string '2024-01-15'. What preprocessing is needed?",
    "How will you handle the class imbalance in Churn?",
    "Write the complete sklearn Pipeline for this dataset.",
    "Which features might you drop and why?",
]
for i, t in enumerate(tasks, 1):
    story.append(Paragraph(f"({i}) {t}", BULLET))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 16 – MEMORY TRICKS & LAST DAY REVISION
# ══════════════════════════════════════════════════════════════════════════════
story += section_header("🧠 SECTION 16: Memory Tricks & Last-Day Revision", colors.HexColor("#b71c1c"))

story += sub_header("Memory Tricks")
tricks = [
    ("IQR Steps", "SQQIF — Sort, Q1, Q3, IQR (Q3-Q1), Fences (±1.5×IQR)"),
    ("Missing Data Types", "MCMAR — MCAR (random), MAR (observed), MNAR (hidden/systematic)"),
    ("Encoding Choice", "Ordinal=Label, Nominal=OHE, High-Cardinality=Target/Binary"),
    ("Scaling Choice", "Outliers present → Z-score | Fixed range needed → Min-Max"),
    ("Join Types", "INNER=intersection, OUTER=union, LEFT=keep left, RIGHT=keep right"),
    ("Pipeline rule", "Fit on TRAIN, Transform ALL — never fit on test set"),
    ("Deletion vs Imputation", "&lt;5% missing → delete rows | &gt;5% → impute"),
    ("Z-score threshold", "68-95-99.7 rule: ±1σ=68%, ±2σ=95%, ±3σ=99.7% — beyond ±3 is outlier"),
]
story += make_table(["Concept","Memory Trick"], tricks)

story += sub_header("📌 KEY FORMULAS — Quick Reference")
formulas = [
    ("IQR", "Q3 - Q1"),
    ("Lower Fence (IQR)", "Q1 - 1.5 × IQR"),
    ("Upper Fence (IQR)", "Q3 + 1.5 × IQR"),
    ("Z-Score", "(X - μ) / σ"),
    ("Min-Max Normalization", "(X - X_min) / (X_max - X_min)"),
    ("Standardization", "(X - μ) / σ"),
    ("Mean", "Σ(Xi) / n"),
    ("Median (even n)", "(n/2-th + (n/2+1)-th) / 2"),
    ("Standard Deviation", "√[Σ(Xi-μ)² / n]"),
]
story += make_table(["Formula Name","Formula"], formulas)

story += sub_header("📋 LAST-DAY REVISION CHECKLIST")
checklist = [
    "✅ Read CSV: pd.read_csv() | Write: df.to_csv(index=False)",
    "✅ Missing types: MCAR (random) | MAR (depends on observed) | MNAR (depends on missing value)",
    "✅ Deletion: dropna() — use for MCAR + small %",
    "✅ Imputation: fillna(mean/median/mode) or sklearn SimpleImputer",
    "✅ IQR outlier: Q1-1.5×IQR to Q3+1.5×IQR | Z-score: |Z|>3",
    "✅ Min-Max: [0,1], sensitive to outliers | Z-score: mean=0 std=1, robust",
    "✅ Label Encoding: ordinal/tree models | OHE: nominal/linear models + drop_first=True",
    "✅ Joins: inner (both), left (left df), right (right df), outer (all)",
    "✅ Pipeline: prevents leakage, reproducible, deployable",
    "✅ Fit scaler on TRAIN data ONLY — transform both train and test",
    "✅ drop_duplicates() — after merging and loading",
    "✅ SMOTE — oversample minority class for imbalance",
    "✅ pivot_table: long→wide | melt: wide→long",
    "✅ Dummy variable trap: always drop_first=True in OHE",
    "✅ Stratified sampling: preserves class ratios in train-test split",
]
for item in checklist:
    story.append(Paragraph(item, BULLET))

story.append(sp(10))
story += info_box(
    "<b>EXAM TIP:</b> For numerical questions, always show your work step by step — "
    "sort the data, compute Q1/Q3/IQR/fences explicitly. Partial marks are given for each step. "
    "For theory questions, use the mnemonic tricks and always give a real-world example.",
    YELLOW_LIGHT, ORANGE
)

# ══════════════════════════════════════════════════════════════════════════════
# BUILD PDF
# ══════════════════════════════════════════════════════════════════════════════
out_path = "/mnt/user-data/outputs/Unit3_Data_Wrangling_Complete_Notes.pdf"

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK_BLUE)
    canvas.rect(0, 0, W, 1.2*cm, fill=1, stroke=0)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(WHITE)
    canvas.drawString(2*cm, 0.45*cm, "Unit III: Data Handling, Wrangling & Preprocessing")
    canvas.drawRightString(W-2*cm, 0.45*cm, f"Page {doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(
    out_path,
    pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2*cm, bottomMargin=1.8*cm,
    title="Unit III – Data Wrangling & Preprocessing",
    author="Topper Notes Generator",
)
doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print("PDF built:", out_path)