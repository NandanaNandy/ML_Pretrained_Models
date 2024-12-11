import spacy
from spacy.training.example import Example
import random

# Step 1: Prepare Training Data
TRAIN_DATA = [
    (
"""BOARD OF SECONDARY EDUCATION
ANDHRA PRADESH
SECONDARY SCHOOL CERTIFICATE
This is to certify that : SANNAPUREDDY NARAYANA REDDY
Father Name : SANNAPUREDDY LAKSHMI REDDY
Registered Number: 0922111776
School Name : Z P HIGH SCHOOL SIDDAVARAM PORUMAMILLA (M)
District Name: KADAPA
has appeared and PASSED SSC EXAMINATION held in : MARCH 2009 in FIRST
Division with TELUGU as medium of instruction.
DATE OF BIRTH
16-Jun-1994
THE CANDIDATE SECURED THE FOLLOWING PERCENTAGE OF MARKS
Marks Secured (in
SUBJECT
Marks Secured (in words)
figures)
NINETY THREE
TELUGU
93
ENGLISH
75
SEVENTY FIVE
MATHEMATICS
90
NINETY
GENERAL SCIENCE
NINETY FOUR
od
SOCIAL STUDIES
EIGHTY EIGHT
88
SIXTY FIVE
HINDI
୧ર
Marks Total :
505
Five Hundred Five
SECRETARY
BOARD OF SECONDARY EDUCATION
don 16-Dop-2021
can download the centificate on clicking
woh I"M Wob LD AI'2/ It whotel
A.P. AMARAVATI
unity Deveload Catill cated Dona
teredli - 8 5CMarks-16122021-06593""",
        {
            "entities": [
    (71, 100, "NAME"),      # "SANNAPUREDDY NARAYANA REDDY"
    (341, 351, "DOB"),      # "16-Jun-1994"
    (566, 569, "TOTAL_MARK")# "505"
    
    
]
        }
    ),
    
    (
        """32241735
சான்றிகழ் விளை
CERTIFICATE SL NO : HSS
தமிழ்நாடு மாநிலப் பள்ளித் தேர்வுகள் குழுமம்
STATE BOARD OF SCHOOL EXAMINATIONS, TAMILNADU
அரசுத் தேர்வுகள் துறை, சென்னை - 600 006
DEPARTMENT OF GOVERNMENT EXAMINATIONS, CHENNAI - 600 006
மேல்நிலைப் பள்ளிக் கல்வி இரண்டாமாண்டு மதிப்பெண் சான்றிதழ்
HIGHER SECONDARY COURSE - SECOND YEAR MARK CERTIFICATE
தமிழ்நாடு அரசின் அதிகாரத்திற்கு உட்பட்டு வழங்கப்படுகிறது
ISSUED UNDER THE AUTHORITY OF THE GOVERNMENT OF TAMILNADU
தேர்வரின் பெயர் / NAME OF THE CANDIDATE
மதிப்பெண் சா
QUIDEALILIL
மோனிகா ரா
மற்றும் வருடம்/SESS
MONIKA R
AND YEAR OF ISSUE OF
MARK CERTIFICATE
பிறந்த தேதி / DATE OF BIRTH
நிரந்தரப் பதிவெண் / PERMANENT REGISTER NUMBER
மே 2022
20/04/2005
2111259295
MAY 2022
மேல்நிலைப் பள்ளிக் கல்வி இரண்டாமாண்டு பொதுத் தேர்வெழுதிய மேற்காண் தேர்வர்
கீழ்க்குறிப்பிட்டுள்ள
பாடங்களில் தேர்வெழுதி தேர்ச்சி பெற்றுள்ளார் எனச் சான்றளிக்கப்படுகிறது
Certified that the above mentioned candidate passed the following subjects in the Higher Secondary Second Year Examination
கருத்தியல்
செய்முறை அகமதிப்பீடு
தேர்ச்சி பெற்ற பருவம், வருடம்
om b
பெற்ற
THEORY
மதிப்பெண்கள் 100 க்கு
PRACTICAL
INTERNAL
SUBJECT
மற்றும் தேர்வெண்
MARKS
70/90
20/75
10/25
SESSION, YEAR AND
OBTAINED FOR 100
ROLL NO, OF PASSING
 தமிழ்
079
010
089
5259406 MAY 2022
TAMIL
ஆங்கிலம்
081
010
091
5259406 MAY 2022
ENGLISH
இயற்பியல்
052
020
010
082
5259406 MAY 2022
PHYSICS
வேதியியல்
065
020
010
095
5259406 MAY 2022
CHEMISTRY
உயிரியல்
059
020
010
089
5259406 MAY 2022
BIOLOGY
கணிதவியல்
083
010
093
5259406 MAY 2022
MATHEMATICS
மொத்த மதிப்பெண்கள் / TOTAL MARKS :
0539
ZERO FIVE THREE NINE
பள்ளியின் பெயர் / SCHOOL NAME
( D41/CMBT0106/041039 )
SVGV MATRIC HR SEC SCHOOL KARAMADAI
எஸ்விஜிவி மெட்ரிக் மேல்நிலை பள்ளி காரமடை
பயிற்றுமொழி / MEDIUM OF INSTRUCTION
பாடத்தொகுப்பு எண் மற்றும் பெயர் / GROUP CODE AND NAME
ENGLISH
GENERAL EDUCATION
பொதுக்கல்வி
1
அ.ம.ப. குறிமீட்டெண் & நாள் / T.M.R.CODE NO.& DATE
2503
A2236130
20.06.2022
EMIS ID No. 3312170130700634
பாரிலப் பள்ளித் தோவுகள் குழுமம் (மேலதி
ாவான தையாப்ப
MEMBER SECRETARY
TE BOARD OF SCHOOL EXAMINATIONS (HR SEC""",
        {
            "entities": [
    (72, 80, "NAME"),         # "MONIKA"
    (161, 171, "DOB"),        # "20/04/2005"
    (535, 539, "TOTAL_MARK")  # "539"
]
        }
    ),
    (
"""
શત માધ્યમિક અને ઉચ્ચતર માધ્યમિક શિક્ષણ બોર્ડ, ગાંદ
at Secondary & Higher Secondar
cation Board, Gandhinagar
D 003334
ગુણવત્રક-ઉચ્ચતર માધ્યમિક પ્રમાણપત્ર પરીક્ષા - 2010
Statement of Marks - Higher Secondary Certificate Examination - 2010
પરીક્ષાઓ માસ અને વર્ષ
Son elore
RHOT BAID
HOM
CENTRE NO.
SCHOOL INDEX NO
MONTH & YEAR OF THE EXAM
STREAM
NO, OF STATEM
MARCH-2010
004
01. 042
GENERAL
603304
CANDIDATE S NAME
Glos Shis
G156615
VAIDYA KISHAN DINESHKUMAR
mile mig = sofe mo = sele upinte late 155
મેળવેલ ગુજ શબ્દીમાં
વિષયનું નામ કોડ નંબર સાથે
MARKS OBTAINER = TOTAL
TOTAL
NAME OF THE SUBJECT WITH CODE NO.
MARKS OBTAINED IN WORDS
MARKS
001 GUJARATI (FIRST LANG)
100
74
SEVEN FOUR
013 ENGLISH (SECOND LANG)
100
80
EIGHT ZERO
055 ECONOMICS
100
90
NINE ZERO
046 DRG. OF COMM.
100
d 5
NINE TWO
135 STATISTICS
100
100
ONE ZERO ZERO
154 ELEMENTS OF ACCT.
100
97
NINE SEVEN
331
COMPUTER
(NEW) - TH
100
Ba
EIGHT MINE
332
COMPUTER
(NEW)
PR
050
50
FIVE ZERO
$
Marks In These Subjects Are
Not
Included
In Total and %
મેળવેલ કુલ ર
પરિણામ
se oper
ટકા
 ऐली
TOTAL MARKS OBTAINED
TOTAL MARKS
RESULT
PERCENTAGE
- GRADE
ess
700
PASS
88. 86
ONE (DISTINCTION
મેળવેલ હુલ ગુણ શબ્દોમાં
SIX HUNDRED TWENTY TWO
TOTAL MARKS OBTAINED IN WORDS
જાગાસન્નું : આ ગુલ્મપત્રકમાં સહી કરનાર સત્તાપિકારી સિવાય કોઈ કેરકાર
ની અને જો કરશે તો ગુજરપત્રક રદ થશે અને બોર્ડ કાયદેસરનાં પગલાં હ
oned which is n
MPORTANT : Any change in this statement, except by
) AO : Indicates 'Ab
authority, will result into cancellation of the statoment and
also invoke imposition of appropriate legal
GRADE : Grade One (With Distinction) : 70% and above
rade One : 60% and above, but below 70%
Grade Two : 45% and above, but below 60%
ade Three : To all other candidates, including the exemple
ing Standard for Disabled students is 20%
(D. S. Patel)
Passing Standard for English - 013 (SL) Subject is 20'
262728470""",
        {
            "entities": [

    (164, 188, "NAME"),        # "VAIDYA KISHAN DINESHKUMAR"

    (340, 350, "DOB"),         # "MARCH-2010"

    (564, 567, "TOTAL_MARK")# "622"

]
        }
    ),
    (
"""
All and States of Street States
SI. No. : 220144
ಭಾರತ್ ಇನ್ನಿಟ್ಯೂಟ್ ಆಫ್ ಸ್ಕೂಲಿಂಗ್ ಎಜುಕೇಷನ್(ರಿ)
BHARATH INSTITUTE OF SCHOOLING EDUCATION(R)
ಕರ್ನಾಟಕ ಸರ್ಕಾರದಿಂದ ಅನುಮತಿ ಮತ್ತು ಮಾನ್ಗತೆ
APPROVED AND RECOGNISED BY GOVERNMENT OF KARNATAKA
ಅಂಕಪಟ್ಟ * ಪ್ರಮಾಣದ
MARKS STATEMENT * CERTIFICATE
ಸಿನಿಯರ್ ಸೆಕೆಂಡರಿ ಎಕಾಮಿನೇಷನ್ (10+2)
SENIOR SECONDARY EXAMINATION (10+2)
ತು ಕೆಳಗೆ ನದುೂದಿಸಿದ ಆದ್ಯರ್ಥಿಯು ಪಿನಿಯರ್ ಸೆಕೆಂಡರಿ ಎಣ್ಣಮರೇಷನ್ (10+2) ಕೋರ್ಡ್‌ನ್ನು ಪೂರ್ಣಗೊಂಬಿ, ಸದರ ಪರೀಕ್ಷೆಯಲ್ಲಿ ಕೆಳಗಿನ
ಎಚರಗಳೊಂದಿಗೆ ತೇರ್ಗಡೆಯಾಗಿರುತ್ತಾರೆ ಎಂದು ಪ್ರಮಾಣಿಕಂಸಲಾಗಿದೆ.
This is to certify that the candidate mentioned below has completed the course and passed the
Senior Secondary Examination (10+2) with the following details.
acrists / CHF
ಅಭ್ಯರ್ಥಯ ಜಿಸರು
AUGUST 2022
PREMA N
Month/Year
Candidate's Name
ನೊ:ಂದಣ ಸಂಪ
ತಾಯಿಯ ಹೆಸರು
LAKSHMI R
Enrollment No. 220ABU01006
Mother's Name
ತಂಜಿಯ ಹೆಸರು
ENGLISH
NARAYANAPPA K M
Medium
Father's Name
ಆಸ ವಿಸಾಂಕ
Date of Birth : 10-01-1999 TEN - JANUARY - ONE THOUSAND NINE HUNDRED NINETY NINE
made come Marks Obtained
BOEHOS
 Hoke
In Words
In Figure
 ಅಕ್ಕರಗಳಲ್ಲಿ
Subject
BOATC
Cade C
carici
(D)
SIX SIX
KANNADA
100
Re
66
B01
58
FIVE EIGHT
100
CRA
(( B02
ENGLISH
SEVEN SEVEN
100
57
770
B21
HISTORY
SEVEN FOUR
74
ECONOMICS
100
74
B22
(a)
SIX SEVEN
POLITICAL SCIENCE
100
B29
FIVE EIGHT
SOCIOLOGY
100
ട્વ
 ব
B28
400
600
ಲಿತಾಂಶ
ಅಂಕಗಳು ಅಕ್ಷರಗಳಲ್ಲಿ
FIRST
4 0 - 0 -
Result:
CLASS
Marks in Words : FOUR ZERO ZERO
Address : No. 52/2 Sharada Arcade, Maruthi Farm,
Dombarahalli, Lakshmipura (P)
Davanapara (11), Bengalura - 562 162.
Controller of Examina
7-10-2022""",
        {
            "entities": [
    (121, 135, "NAME"),        # "PREMA N"
    (172, 190, "DOB"),         # "10-01-1999"
    (589, 592, "TOTAL_MARK")# "400"
]
        }
    ),
    (
        """
GOVERNMENT OF KERALA
BOARD OF HIGHER SECONDARY EXAMINATION
HIGHER SECONDARY EXAMINATION (CLASS XII)
No. HSE 0325184
CERTIFICATE
Register
Number
This is to certify that Mr/Ms ... MOHAMMED SHAHIK, E.P.
.. appeared for the
HIGHER SECONDARY EXAMINATION ( COMMERCE
GROUP) held in . MARCH ZOO4
He/She ........ PASSED the Examination in Second Class.
The marks obtained by the Candidate are shown below :
Min.
Marks Obtained
Max.
Marks
SUBJECTS
In figures
Marks
Required
In words
Subject Part Total
for Pass
ENGLISH
38
38
Three Eight
35
100
MALAYALAM
75
75 Seven Five
35
100
PART III (Optionals)
BUSINESS STUDIES MITH
100
43
43
Four Three
35
FUNCTIONAL MANAGEMENT
ACCOUNTANCY WITH
53
100
53
Five Three
35
AFS/COSTING
ECONOMICS
51
51 Five One
35
100
POLITICAL SCIENCE
51
Five One
35
100
51
198 One Nine Eight
140
400
TOTAL FOR PART III
311
Three One One
210
600
GRAND TOTAL (PARTS 1+II+II)
ations).
John Director (
Exami
Place > Thiruvananthapuram
Department of Higher Secondary Education,
Date : 18/05/2004
Government of Kerala.""",
        {
            "entities": [
    (52, 68, "NAME"),        # "MOHAMMED SHAHIK"
    (184, 192, "DOB"),       # "MARCH 2004"
    (491, 494, "TOTAL_MARK")# "311"
]
        }
    ),
    (
        """GOVERNMENT OF KERALA
BOARD OF HIGHER SECONDARY EXAMINATION
HIGHER SECONDARY EXAMINATION (CLASS XII)
Register
No. HSE 282240
682766
CERTIFICATE
Number
This is to certify that Mr/Ms. FAISAL ... C. A ...
... has appeared for the
HIGHER SECONDARY EXAMINATION ( SCIENCE
GROUP) heldMarch ... 2002 ...
He/She has ... PASSED the Examination in Second Class ............
The marks obtained by the Candidate are shown below :
Marks Obtained
Min.
Max.
SUBJECTS
In figures
In words
Marks
Marks
Subject | Part Total
PART I
78 Seven Eight
53
78
150
ENGLISH
PART II
53
150
dd
94 Nine Four
HINDI
PART III (Optionals)
100
PHYSICS
Theory
35
30
Practical
26
50
ട്ട്
150
Total
61
Theory
30
100
CHEMISTRY
୧୫
Practical
37
50
ട് 3
150
Total
105
BIOLOGY
Theory
56
30
100
42
Practical
50
ട്ട്
Total
dB
150
53
150
MATHEMATICS
83
347
Three Four Seven
212
600
TOTAL FOR PART III
GRAND TOTAL (PARTS I+II+II)
519 Five One Nine
318
900
Joint Director (Examinations),
Place : Thiruvananthapuram
Department of Higher Secondary Education,
Date : 20/06/2002
Government of Kerala.""",
        {
            "entities": [
    (88, 102, "NAME"),         # "FAISAL C. A"
    (217, 223, "DOB"),         # "MARCH 2002"
    (574, 577, "TOTAL_MARK")# "519"
]
        }
    ),
    (
"""
Modern Education Society, Pune
Name of the Institution
D. G. Ruparel College of Arts, Science & Commerce
Name of the College
and and the consider and the considered to the may be and
राज्य माध्यमिक व उच्च माध्यमिक शिक्षण
Alaharashtra State Board
Digher Secondary Couration
rondary and
विभागीय मंडळ / MUMBAI DIVISIONAL BOARD
उच्च माध्यमिक प्रमाणपत्र प
HIGHER SECONDARY CERTIFICATE EXAMINATION
STATEMENT OF MARKS
परीक्षेचा महिना व वर्ष
आसन क्रमांक
केंद्र कमांक
जिल्हा व उच्च माध्य शाळा क्रमाक
शाखा
गुणपत्रिकेचा अनुक्रमांक
SEAT NO.
CENTRE NO.
DIST. & HR. SEC. SCHOOL NO.
STREAM
MONTH & YEAR OF EXAM
SR. NO. OF STATEMENT
M137509
ARTS
3304
31.05.014
208943
FEBRUARY-18
उमेदवाराचे संपूर्ण नाव (आडनाव प्रथम ) / CANDIDATE'S FULL NAME (SURNAME FIRST)
Erayan Roshani Azadkaran
उमेदवाराच्या आईचे नाव / CANDIDATE'S MOTHER'S NAME
Bharati
कमाल
विषयाचा सांकेतिक क्रमाक व विषयाचे नाट
प्राप्त गुण / Marks Obtained
* माध्यम
गुण
Subject Code No. and Subject Name
Max.
 अंकात
In Figures
Medium
अक्षरात / In Words
Marks
01 ENGLISH
ENG
100
070
SEVENTY
04 HINDI
HIN
100
077
SEVENTYSEVEN
38 HISTORY
ENG
100
068
SIXTYEIGHT
47 LOGIC
ENG
100
075
SEVENTYFIVE
48 PSYCHOLOGY
ENG
100
063
SIXTYTHREE
49 ECONOMICS
ENG
100
061
SIXTYONE
31 ENVIRONMENT EDUCATION
ENG
050
036
THIRTYSIX
30 HEALTH & PHYSICAL EDUCATION (GRADE)
A
Result / निकाल
Percentage / टक्केवारी
एकूण गुण /
PASS
69.23
FOUR HUNDRED AND
650
450
Total Marks
FIFTY
H184208943
1, 4, 268055191,
रिक शिक्षण विषयातील श्रेणी
यांचा तपशील मागील पृष्ठावर पहावा.
lportant, Notes, Grades in Health &
lai Education Subject and meaning of special
विभागीय  सचिव / Divisional Secretary""",
        {
            "entities": [
    (140, 156, "NAME"),         # "Erayan Roshani Azadkaran"
    (167, 174, "MOTHER_NAME"),  # "Bharati"
    (451, 453, "TOTAL_MARK")    # "650"
]
        }
    ),
    (
"""
हाराष्ट्र राज्य माध्यमिक व उच्च माध्यमिक शिक्षण मं
Maharashtra State Board Of
Secondary and Higher Secondary Education,
भागीय मंडळ / MUMBAI DIVISIONAL BOARD
nध्यामक प्रमाणपत्र परीक्षा
गणपत्रक
HIGHER SECONDARY CERTIFICATE EXAMINATION
- STATEMENT OF MARKS
शाखा
दिल्ला व रख मान्य माना कमांक
न्द क्रमांक
आम्मन क्रमांक
यरीक्षेचा पहिना व वर्ष
याणाविकवा अनुक्रमाक
STREAM
SEAT NO
CENTRE NO.
DIST.& HR.SEC.SCHOOL NO
MONTH & YEAR OF EXAM.
SR NO. OF STATEMENT
SCIENCE
M004935
1051
16.14.045
029364
र्ग नाव (आडनाव प्रथम) / CANDIDATE'S FULL NAME (SURNAME FIRST)
Ghosh Rakesh Nikhil
उमेदवाराच्या आईचे नाव / CANDIDATE'S MOTHER'S NAME
Gouri
विषयाचा मांकेतिक क्रमांक व विषयाचे नाव
कमाल
प्राप्त गुण / Marks Obtained
* पाध्यम
गण
Subject Code No. and Subject Name
अंकात
Medium
Max.
अक्षरात / In Words
In Figures
Marks
01 ENGLISH
ENG
100
073
SEVENTYTHREE
48 PSYCHOLOGY
ENG
100
061
SIXTYONE
54 PHYSICS
ENG
100
073
SEVENTYTHREE
55 CHEMISTRY
ENG
100
063
SIXTYTHREE
56 BIOLOGY
ENG
100
080
EIGHTY
97 INFORMATION TECHNOLOGY(SCI)
ENG
100
089
EIGHTYNINE
31 ENVIRONMENT EDUCATION
ENG
050
048
FORTYEIGHT
30 HEALTH & PHYSICAL EDUCATION (GRADE)
A
टक्केवारी / Percentage
एकूण गुण ।
FOUR HUNDRED AND
74.92
650
487
Total Marks
EIGHTYSEVEN
निकाल / Result
PASS
H204029364
4421599315560
महत्वाचे, टीप, आरोग्य व शामीरिक शिक्षण विषयानील श्रेणी
आणि चिन्हांची माहिती यांचा तपशील मागील पृथ्ठावा पहावा.
See overleaf for Important, Notes, Grades in Health &
Physical Education Subject and meaning of special
विभागीय सचिव/Divisional Secretary
characters.""",
        {
            "entities": [
    (148, 171, "NAME"),            # "Ghosh Rakesh Nikhil"
    (181, 185, "MOTHER_NAME"),      # "Gouri"
    (478, 480, "TOTAL_MARK"),       # "487"
    (537, 539, "PERCENTAGE")   # "74.92"
]
        }
    ),
    ("""
சான்றிதழ் வ. எண்
13705958
CERTIFICATE SL. NO. HSG
ிழ்நாடு மாநிலப் பள்ளித் தேர்வுகள் குழுமம்
OARD OF SCHOOL EXAMINATIONS, TAN
அரசுத் தேர்வுகள் துறை, சென்னை - 600 006
DEPARTMENT OF GOVERNMENT EXAMINATIONS, CHENNAI - 600 006
மேல்நிலைப் பள்ளிக் கல்விச் சான்றிதழ்
HIGHER SECONDARY COURSE CERTIFICATE
பொதுக்கல்வி / GENERAL EDUCATION
தமிழ்நாடு அரசின் அதிகாரத்திற்கு உட்பட்டு வழங்கப்படுகிறது
ISSUED UNDER THE AUTHORITY OF THE GOVERNMENT OF TAMILNADU
தேர்வரின் பெயர் / NAME OF THE CANDIDATE
LI(Thain / SESSION
தனுஷ்வர்தன் செ
மார்ச் 2018
DHANUSHWARDHAN S
MAR 2018
மேல்நிலைப் பள்ளிக் கல்விப் பொதுத் தேர்வெழுதிய மேற்காண் தேர்வர் கீழ்க்காணும் மதிப்பெண்களைப்
பெற்றுள்ளார் என்று சான்றளிக்கப்படுகிறது.
Certified that the above mentioned candidate appeared for the Higher Secondary Public Examination
and obtained the following marks :
um_ம்
கருத்தியல்
செய்முறை
பெற்ற மதிப்பெண்கள் 200 க்கு
PRAC.
SUBJECT
MARKS OBTAINED FOR 200
தமிழ்
TAMIL
155
ONE FIVE FIVE
(P)
ஆங்கிலம்
ENGLISH
152
ONE FIVE TWO
(P)
இயற்பியல்
PHYSICS
100
050
150
ONE FIVE ZERO
(P)
வேதியியல்
CHEMISTRY
069
050
119
ONE ONE NINE
(P)
கணிப்பொறி இயல்
COMPUTER SCIENCE
119
050
169
ONE SIX NINE
(P)
கணிதவியல்
MATHEMATICS
105
ONE ZERO FIVE
(P)
மொத்த மதிப்பெண்கள் / TOTAL MARKS :
ZERO EIGHT FIVE ZERO
0850
பிறந்த தேதி / DATE OF BIRTH
தேர்வெண்/ EXAM NO.
அ. ம. ப. குறியீட்டெண் & நாள் / TMR CODE NO. & DATE
07.11.2000
1781980
G1717937
16.05.2018
நிரந்தரப் பதிவெண் / PERMANENT REGISTER NO.
பயிற்று மொழி / MEDIUM OF INSTRUCTION பாடத்தொகுப்பு எண் / GROUP CODE
1811781980
ENGLISH
102
பள்ளியின் பெயர் / NAME OF THE SCHOOL
(63/PRI516/6349)
புனித அன்னாள் பதின்ம மேல்நிலைப் பள்ளி மாதவரம், சென்னை
ST.ANN'S MATRIC HR SEC SCHOOL MADHAVARAM, CHENNAI
உறுப்பினர் செயலர்
மாநிலப் பள்ளித் தேர்வுகள் குழுமம் (மேல்நிலை), தமிழ்நாடு
வரின் கையொப்பம்
MEMBER SECRETARY
SIGNATURE OF THE CANDIDATE
STATE BOARD OF SCHOOL EXAMINATIONS (HR.SEC), TAMILNAD""",
        {
            "entities": [
    (216, 244, "CANDIDATE_NAME"),        # "DHANUSHWARDHAN S"
    (432, 436, "TOTAL_MARKS"),           # "0850"
    (459, 467, "DATE_OF_BIRTH")          # "07.11.2000"
]
        }
    ),
            (
        """சான்றிது வ. எண்
CERTIFICATE SL. NO. HS
மிழ்நாடு மாநிலப் பள்ளித் தேர்வுகள் குழு
OARD OF SCHOOL EXAMINATIONS, TAM
அரசுத் தேர்வுகள் துறை, சென்னை - 600 006
DEPARTMENT OF GOVERNMENT EXAMINATIONS, CHENNAI - 600 006
மேல்நிலைப் பள்ளிக் கல்விச் சான்றிதழ்
HIGHER SECONDARY COURSE CERTIFICATE
பொதுக்கல்வி / GENERAL EDUCATION
தமிழ்நாடு அரசின் அதிகாரத்திற்கு உட்பட்டு வழங்கப்படுகிறது
ISSUED UNDER THE AUTHORITY OF THE GOVERNMENT OF TAMILNADU
தேர்வரின் பெயர் / NAME OF THE CANDIDATE
பருவம் / SESSION
அனிதா 8
LORGE 2017
MAR 2017
ANITHA S
மேல்நிலைப் பள்ளிக் கல்விப் பொதுத் தேர்வெழுதிய மேற்காண் தேர்வர் கீழ்க்காணும் மதிப்பெண்களைப்
பெற்றுள்ளார் என்று சான்றளிக்கப்படுகிறது.
Certified that the above mentioned candidate appeared for the Higher Secondary Public Examination
and obtained the following marks :
கருத்தியல்
 செய்யுறை
பெற்ற மதிப்பெண்கள் 200 க்கு
um ம்
PRAC
SUBJECT
THEORY
MARKS OBTAINED FOR 200
150
 50
NIBED
195
ONE NINE FIVE
(P)
TAMIL
ஆங்கிலம்
188
ONE EIGHT EIGHT
(P)
ENGLISH
இயற்பியல்
150
050
200
TWO ZERO ZERO
(P)
PHYSICS
Gas Bullus
ONE NINE NINE
(P)
149
050
199
CHEMISTRY
= (Sidlus)
050
ONE NINE FOUR
(P)
144
194
BIOLOGY
கணிதவியல்
TWO ZERO ZERO
200
(P)
MATHEMATICS
மொத்த மதிப்பெண்கள் / TOTAL MARKS :
1176
ONE ONE SEVEN SIX
அ. ம. ப. குறியீட்டெண் & நான் / TMR CODE NO. & DATE
தேர்வெண் / ROLL NO.
பிறந்த தேதி / DATE OF BIRTH
G544658
12.05.2017
05.03.2000
494361
பாடத்தொகுப்பு எண் / GROUP CODE
நீரந்தரப் பதிவெண் / PERMANENT REGISTER NO.
LILS MILL MEDIUM OF INSTRUCTION
103
1710484361
TAMIL
Usinsflußleir Gluilit / NAME OF THE SCHOOL
( 41 \ PBR413 \ 4122 )
 ராஜவிக்னேஷ் மேல்நிலைப் பள்ளி மேலமாத்தூர் அஆலத்தூர் (வ/பெரம்பலூர்
RAJAVIGNESH HR SEC SCHOOL MELAMATHUR PO PERAMBALUR DT
றுப்பினர் செயலா்
d . 2000 151
மாநிலப் பள்ளித் தேர்வுகள் குழுமம் (மேல்நிலை), தமிழ்நாடு
தேர்வரின் கையொப்பம்
MEMBER SECRETARY
SIGNATURE OF THE CANDIDATE
STATE BOARD OF SCHOOL EXAMINATIONS (HR.SEC), TAMILNADU""",
        {
            "entities": [
    (120, 131, "CANDIDATE_NAME"),       # "ANITHA S"
    (513, 517, "TOTAL_MARKS"),          # "1176"
    (570, 578, "DATE_OF_BIRTH")         # "05.03.2000"
]
        }
    ),
    
    (
    """

माक (Sr. No.)
0898138
2200052
स्राईस्कूल परीक्षा-२०१३
High School Examination-2013
- सह-अंकपत्र (CERTIFICATE-CUM-MARKS SHEET)
प्रमाणपत्र क्रमांक
परीक्षा प्रवर्ग
जनपद/कोन्द्र/विद्यालय कोड
संस्थागत् व्यक्तिगत्
अनुक्रमांक
Certificate No.
Exam. Type
Regular / Private
Roll No.
Distt./Centre/School Code
2250052
FULL EXAM
REGULAR
0874774
22/15698/1205
प्रभाणित किया जाता है कि (This is to certify that)
ROHIT SAGAR
परिषद् के अभिलेखानुसार (according to the Board's record)-
आत्मज/आत्मजा श्रीमती (son/daughter of Mrs.) KIRAN DEVI
MAHIPAL SINGH
एवं श्री (and Mr.)-
19TH JULY (WRETER HUNDRED NINETY NINE (19-07-99)
(has passed High School Examination held in March/April 2013
ren विद्यालय/केन्द्र
ने मार्च/अप्रैल 2013 की
SITARAM H S S SABDALPUR SHARKI J P NAGAR
from School/Centre)-
निष्न विवरणानुसार उत्तीर्ग की से youn the totlowing details).
ग्रेड |
परीक्षाफल
प्राप्तांक Obtained Marks
अधिकतम अंक
योग
विषय
Grade
Result
से द्वान्तिक (Theory) प्रयोगात्मक (Practical)
Total
Max, Marks
Subject
053
030
083
A2
100
HINDI
077
B1
047
030
100
ENGLISH
PASSED
078
B1
100
046
030
MATHEMATICS
100
SCIENCE
050
030
080 4
B1
SOCIAL SCIENCE
100
054
030
084
A2
100
DRAWING
093
064
029
A1
No divisions are awarded
A
Category of Moral, Sports and Physical Education-
8TH JUNE, 2013
तिथि (Date)-
स्थान (Place)- Allahabad, Uttar Pradesh
(Upendra Kun
Note : For Important Instructions see overleaf.
माचव (Secreti
""",
        {
            "entities": [
    (9, 23, "CANDIDATE_NAME"),       # "ROHIT SAGAR"
    (174, 176, "TOTAL_MARKS"),       # "083"
    (305, 315, "DATE_OF_BIRTH")      # "19TH JULY (WRETER HUNDRED NINETY NINE (19-07-99)"
]
        }
    ),
    
      (
"""
1519504
M222/55421/0066
SENIOR S
यह प्रमाणित किया जाता है कि
This is to certify that HARI BABU R
अनुक्रमांक
Roll No.
20662612
माता का नाम
Mother's Name
SUMATHI K
पिता/संरक्षक का नाम
Father's / Guardian's Name RAVI KUMAR R
विद्यालय
School
55421
SRI CHAITANYA TECHNO SCHOOL COIMBATORE TN
की शैक्षणिक उपलब्धियां निम्नानुसार हैं has achieved Scholastic Achievements as under :
प्राप्ताक MARKS OBTAINED
 कांड
ERST
POSITIONAL
SUB.
प्रा. /PR.
योग
योग (शब्दो में)
SUBJECT
GRADE
CODE
THEORY
आ.म. IA
TOTAL
TOTAL (IN WORDS)
301
ENGLISH CORE
069
019
088
EIGHTY EIGHT
A2
041
MATHEMATICS
032
020
052
FIFTY TWO
C2
042
PHYSICS
026
028
054
FIFTY FOUR
D2
043
CHEMISTRY
040
028
068
SIXTY EIGHT
C1
COMPUTER SCIENCE (NEW)
083
054
028
082
EIGHTY TWO
B2
500
WORK EXPERIENCE
A2
HEALTH & PHYSICAL EDUCATION
502
A2
GENERAL STUDIES
A2
503
परिणाम Result
PASS
ली Delhi
22-07-2022
TCS Dated :
शैक्षिक उपलब्धियां : सह-शैक्षिक एवम् अनुशासन क्षेत्र में ग्रेडिंग विद्यालय द्वारा अपने स्तर पर बोर्ड द्वारा जारी प्रारामनुसार प्रदान की जाती है
nolastic achievements : Grading for Co-Scholastic and Discipline area is being issued by the so""",
        {
            "entities": [

    (39, 51, "CANDIDATE_NAME"),       # "HARI BABU R"

    (126, 129, "TOTAL_MARKS"),        # "301"

    (180, 188, "DATE_OF_BIRTH")       # "22-07-2022"

]
        }
    ),
      (
        "Candidate name: John Doe. Date of birth: 15-07-1990. Total marks: 85%",
        {
            "entities": [
                (16, 24, "NAME"),       # "John Doe" as NAME
                (41, 51, "DOB"),        # "15-07-1990" as DOB
                (66, 68, "TOTAL_MARK")  # "85" as TOTAL_MARK
            ]
        }
    ),
      (
        """32119941
தமிழ்நாடு மாநிலப் பள்ளித் தேர்வுகள் குழுமம்
STATE BOARD OF SCHOOL EXAMINATIONS, TAMILNADU
அரசுத் தேர்வுகள் துறை.  சென்னை - 600 006
DEPARTMENT OF GOVERNMENT EXAMINATIONS, CHENNAI - 600 006
மேல்நிலைப் பள்ளிக் கல்வி இரண்டாமாண்டு மதிப்பெண் சான்றிதழ்
HIGHER  SECONDARY COURSE - SECOND YEAR MARK CERTIFICATE
தமிழ்நாடு அரசின் அதிகாரத்திற்கு உட்பட்டு வழங்கப்படுகிறது
ISSUED  UNDER  THE  AUTHORITY  OF  THE  GOVERNMENT  OF  TAMILNADU
தேர்வரின் பெயர் / NAME OF THE CANDIDATE
இராஜேஷ் ச
RAJESH S
MARK CERTIFICA
நிரந்தரப் பதிவெண்  /  PERMANENT REGISTER NUMBER
பிறந்த தேதி / DATE OF BIRTH
மே 2022
15/04/2005
MAY 2022
2111119945
தேர்வர் கீழ்க்குறிப்பி.
மேல்நிலைப் பள்ளிக் கல்வி இரண்டாமாண்டு பொதுத் தேர்வெழுதிய மேற்காண்
பாடங்களில் தேர்வெழுதி தேர்ச்சி பெற்றுள்ளார் எனச் சான்றளிக்கப்படுகிறது.
Certified that the above mentioned candidate passed the following subjects in the Higher Secondary Second Year Examination
செய்முறை
அகமதிப்பீடு
கருத்தியல்
மகிப்பெண்கள் 100 க
மற்றும் தோடுவ
INTERNAL
PRACTICAL
THEORY
MARKS
ESSION, YEAR A
10/25
20/75
70/90
OBTAINED FOR 100
ROLL NO. OF PASSING
தமிழ்
5119714 MAY 2022
010
084
074
TAMIL
ஆங்கிலம்
5119714 MAY 2022
010
080
070
ENGLISH
இயற்பியல்
5119714 MAY 2022
010
084
020
054
PHYSICS
வேதியியல்
5119714 MAY 2022
010
096
066
020
CHEMISTRY
உயிரியல்
086
5119714 MAY 2022
010
020
056
BIOLOGY
கணிதவியல்
010
083
5119714 MAY 2022
073
MATHEMATICS
மொத்த மதிப்பெண்கள் / TOTAL MARKS :
0513
ZERO FIVE ONE THREE
பள்ளியின் பெயர் / SCHOOL NAME
( 020/SVPR0032/020011 )
N A ANNAPPARAJA MEMORIAL HR SEC SCHOOL RAJAPALAYAM
ந.அ.அன்னப்பராஜா நினைவு மேல்நிலைப் பள்ளி
இராஜபாளையம்
பயிற்றுமொழி / MEDIUM OF INSTRUCTION
பாடத்தொகுப்பு எண் மற்றும் பெயர் / GROUP CODE AND NAME
TAMIL
பொதுக்கல்வி
/ GENERAL EDUCATION
அ.ம.ப. குறியீட்டெண் & நாள் / T.M.R.CODE NO & DATE
2503
20.06.2022
A2111048
EMIS ID No. 3326061277500257
பிரிகள் செயலர்
மாநிலப் பள்ளித் தேர்வுகள் குழுமம் (மேல்நிலை) குமிட்
தேர்வரின் கையொப்பம்
MEMBER SECRETARY
STATE BOARD OF SCHOOL EXAMINATIONS (HR.S
SIGNATURE OF THE CANDIDA
a for the first for firm and on any and on any and on a comment on a co""",
        {
            "entities": [
    (5, 13, "CANDIDATE_NAME"),       # "RAJESH S"
    (128, 138, "DATE_OF_BIRTH"),     # "15/04/2005"
    (188, 192, "TOTAL_MARKS"),       # "513"
    (285, 345, "SCHOOL_NAME"),       # "N A ANNAPPARAJA MEMORIAL HR SEC SCHOOL RAJAPALAYAM"
]
        }
    )
    # Add more examples for better accuracy
]

for entity in TRAIN_DATA:
    text, dataset = entity
    for start, end, label in dataset["entities"]:
        if start >= end:
            print(f"Invalid entity: {text[start:end]}")
        else:
            print(f"Entity: {text[start:end]}, Label: {label}")

exit()

# # Step 2: Initialize the NLP Model
# # Load a pre-trained model or create a blank one
# nlp = spacy.load("en_core_web_lg")  # or spacy.blank("en") for a blank model

# # Add the NER component to the pipeline if it's not already present
# if "ner" not in nlp.pipe_names:
#     ner = nlp.add_pipe("ner", last=True)
# else:
#     ner = nlp.get_pipe("ner")

# # Step 3: Add Labels to the NER Component
# # Add custom labels to the NER component
# for _, annotations in TRAIN_DATA:
#     for ent in annotations["entities"]:
#         ner.add_label(ent[2])

# # Step 4: Train the Model
# # Disable other pipeline components to focus on training the NER
# other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
# with nlp.disable_pipes(*other_pipes):
#     optimizer = nlp.initialize()  # Correct initialization
#     for epoch in range(30):  # Adjust epochs as needed
#         random.shuffle(TRAIN_DATA)
#         losses = {}
#         for text, annotations in TRAIN_DATA:
#             example = Example.from_dict(nlp.make_doc(text), annotations)
#             nlp.update([example], drop=0.5, losses=losses)  # Adjust drop rate if needed
#         print(f"Losses at epoch {epoch}: {losses}")

# # Step 5: Save the Trained Model
# # Save the model to a directory
# nlp.to_disk("E:\ML_Pretrained_Models\Spacy_models")
# print("Model saved!")

# # Step 6: Test the Model
# # Load the trained model
# custom_nlp = spacy.load("E:\ML_Pretrained_Models\Spacy_models")

# # Test with new text
# test_text = """32396331
# சான்றிதழ் வ. எண்
# CERTIFICATE SL. NO : HSS
# தமிழ்நாடு மாநிலப் பள்ளித் தேர்வுகள் குழுமம்
# STATE BOARD OF SCHOOL EXAMINATIONS, TAMILNADU
# அரசுத் தேர்வுகள் துறை, சென்னை - 600 006
# DEPARTMENT OF GOVERNMENT EXAMINATIONS, CHENNAI - 600 006
# மேல்நிலைப் பள்ளிக் கல்வி இரண்டாமாண்டு மதிப்பெண் சான்றிதழ்
# HIGHER SECONDARY COURSE - SECOND YEAR MARK CERTIFICATE
# தமிழ்நாடு அரசின் அதிகாரத்திற்கு உட்பட்டு வழங்கப்படுகிறது
# ISSUED UNDER THE AUTHORITY OF THE GOVERNMENT OF TAMILNADU
# தேர்வரின் பெயர் / NAME OF THE CANDIDATE
# மதிப்பெண் சான்றிதழ்
# வழங்கப்பட்ட பருவம்
# வெள்ளியங்கிரி பெ
# மற்றும் வருடம்/SESSION
# VELLIYANGIRI P
# AND YEAR OF ISSUE OF
# MARK CERTIFICATE
# நிரந்தரப் பதிவெண் / PERMANENT REGISTER NUMBER
# பிறந்த தேதி / DATE OF BIRTH
# மே 2022
# 26/01/2005
# 2111360426
# MAY 2022
# மேல்நிலைப் பள்ளிக் கல்வி இரண்டாமாண்டு பொதுத் தேர்வெழுதிய மேற்காண் தேர்வர்
# கீழ்க்குறிப்பிட்டுள்ள
# பாடங்களில் தேர்வெழுதி தேர்ச்சி பெற்றுள்ளார் எனச் சான்றளிக்கப்படுகிறது
# Certified that the above mentioned candidate passed the following subjects in the Higher Secondary Second Year Examination.
# கருத்தியல் | செய்முறை அகமதிப்பீடு
# ெற்ற 
# மதிப்பெண்கள் 100 க்கு
# தேர்ச்சி பெற்ற பருவம், வருடம்
# um to
# THEORY
# PRACTICAL
# INTERNAL
# மற்றும் தேர்வெண்
# SUBJECT
# MARKS
# SESSION, YEAR AND
# 70/90
#  20/75
# 10/25
# OBTAINED FOR 100
# ROLL NO. OF PASSING
# தமிழ்
# 086
# 010
# 096
# 5360627 MAY 2022
# TAMIL
# ஆங்கிலம்
# 010
# 070
# 060
# 5360627 MAY 2022
# ENGLISH
# இயற்பியல்
# 048
# 020
# 010
# 078
# 5360627 MAY 2022
# PHYSICS
# வேதியியல்
# 058
# 020
# 010
# 088
# 5360627 MAY 2022
# CHEMISTRY
# உயிரியல்
# 051
# 020
# 010
# 081
# 5360627 MAY 2022
# BIOLOGY
# கணிதவியல்
# 074
# 010
# 084
# 5360627 MAY 2022
# MATHEMATICS
# மொத்த மதிப்பெண்கள் / TOTAL MARKS :
# 0497
# ZERO FOUR NINE SEVEN
# பள்ளியின் பெயர் / SCHOOL NAME
# ( 055/TCGE0078/055040 )
# KANDASWAMI KANDAR'S HIGHER SECONDARY SCHOOL VELUR
# கந்தசாமிக் கண்டர் மேல்நிலைப்பள்ளி, வேலூர்
# பயிற்றுமொழி / MEDIUM OF INSTRUCTION
# பாடத்தொகுப்பு எண் மற்றும் பெயர் / GROUP CODE AND NAME
# TAMIL
# பொதுக்கல்வி
# /
# GENERAL EDUCATION
# அ.ம.ப. குறியீட்டெண் & நாள் / T.M.R.CODE NO.& DATE
# 2503
# A2323795
# 20.06.2022
# EMIS ID No. 3309140220300028
# மாநிலப் பள்ளித் தேர்வுகள் குழுமம் (மேல்நிலை) தமிழ்
# MEMBER SECRETARY
# E OF THE CAND
# STATE BOARD OF SCHOOL EXAMINATIONS (HR.SEC) TAMILNADU"""
# doc = custom_nlp(test_text)

# print("Entities found:")
# for ent in doc.ents:
#     print(f"Entity: {ent.text}, Label: {ent.label_}")
