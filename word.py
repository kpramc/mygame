import pandas as pd

# Data extracted from the previous steps, corrected to ensure all clues are in Tamil
data = {
    "Category": [],
    "Keyword": [],
    "Clue 1": [],
    "Clue 2": [],
    "Clue 3": []
}

three_letter_words = [
    ("அம்பு", "வில்", "எய்", "கூர்மை"),
    ("அரசி", "ராணி", "ராஜா", "கிரீடம்"),
    ("அரிசி", "நெல்", "சோறு", "தானியம்"),
    ("அரிமா", "சிங்கம்", "காடு", "கர்ஜனை"),
    ("அருவி", "நீர்வீழ்ச்சி", "மலை", "தண்ணீர்"),
    ("அன்பு", "பாசம்", "நேசம்", "காதல்"),
    ("அன்னை", "தாய்", "அம்மா", "பெற்றோர்"),
    ("அனல்", "வெப்பம்", "சூடு", "நெருப்பு"),
    ("ஆண்டு", "வருடம்", "மாதம்", "நாள்"),
    ("ஆவணி", "மாதம்", "தமிழ்", "ஐந்தாம்"),
    ("இரவு", "பகல்", "இருள்", "நிலா"),
    ("ஈட்டி", "வேல்", "ஆயுதம்", "திரிசூலம்"),
    ("உண்மை", "பொய்", "மெய்", "சத்தியம்"),
    ("உரிமை", "கடமை", "சுதந்திரம்", "தகுதி"),
    ("உதவி", "சகாயம்", "ஆதரவு", "கைம்மாறு"),
    ("ஐயம்", "சந்தேகம்", "தெளிவு", "கேள்வி"),
    ("ஓய்வு", "உழைப்பு", "இளைப்பாறு", "விடுமுறை"),
    ("கடல்", "சமுத்திரம்", "அலை", "கப்பல்"),
    ("கபடி", "விளையாட்டு", "ஆட்டம்", "குழு"),
    ("கயிறு", "வடம்", "கட்டு", "இழு"),
    ("கரம்", "கை", "விரல்", "உள்ளங்கை"),
    ("கருவி", "சாதனம்", "உபகரணம்", "ஆயுதம்"),
    ("கல்வி", "படிப்பு", "ஞானம்", "பள்ளி"),
    ("கவலை", "துக்கம்", "மகிழ்ச்சி", "துன்பம்"),
    ("கனவு", "நிஜம்", "உறக்கம்", "கற்பனை"),
    ("கிணறு", "கேணி", "தண்ணீர்", "ஆழம்"),
    ("காகம்", "காக்கை", "பறவை", "கரைதல்"),
    ("காலம்", "நேரம்", "பருவம்", "வினாடி"),
    ("காவிரி", "ஆறு", "நதி", "தண்ணீர்"),
    ("கிருமி", "நுண்ணுயிர்", "தோற்று", "நோய்"),
    ("குணம்", "பண்பு", "இயல்பு", "நடத்தை"),
    ("குருவி", "சிட்டு", "பறவை", "கூடு"),
    ("குளம்", "ஏரி", "நீர்நிலை", "தாமரை"),
    ("குளிர்", "வெப்பம்", "பனி", "சளி"),
    ("கேள்வி", "பதில்", "வினா", "விசாரணை"),
    ("கொள்கை", "கோட்பாடு", "தத்துவம்", "விதி"),
    ("கோட்டை", "அரண்", "மதில்", "பாதுகாப்பு"),
    ("கோயில்", "ஆலயம்", "தேவாலயம்", "வழிபாடு"),
    ("சட்டை", "உடை", "ஆடை", "துணி"),
    ("சாட்டை", "அடி", "கசை", "வண்டி"),
    ("சாதம்", "சோறு", "அன்னம்", "உணவு"),
    ("சிற்பி", "சிலை", "செதுக்கு", "உளி"),
    ("ஞாயிறு", "சூரியன்", "கிழமை", "பகல்"),
    ("தந்தை", "அப்பா", "பெற்றோர்", "மகன்"),
    ("தவம்", "யோகம்", "முனிவர்", "வரம்"),
    ("தவறு", "சரி", "பிழை", "குற்றம்"),
    ("தாமரை", "மலர்", "குளம்", "இலை"),
    ("தேசம்", "நாடு", "தேசபக்தி", "குடிமகன்"),
    ("தேர்வு", "பரீட்சை", "வெற்றி", "தோல்வி"),
    ("தோல்வி", "வெற்றி", "பின்னடைவு", "ஏமாற்றம்"),
    ("நகம்", "விரல்", "கை", "கால்"),
    ("நன்றி", "உபகாரம்", "பாராட்டு", "செய்நன்றி"),
    ("நாகம்", "பாம்பு", "சர்ப்பம்", "விஷம்"),
    ("நிலவு", "சந்திரன்", "இரவு", "வெளிச்சம்"),
    ("நிழல்", "வெயில்", "மரம்", "உருவம்"),
    ("நீராவி", "ஆவி", "வெப்பம்", "கொதி"),
    ("பகல்", "இரவு", "வெளிச்சம்", "காலை"),
    ("பல்லி", "ஊர்வன", "சுவர்", "பூச்சி"),
    ("பட்டு", "ஆடை", "துணி", "மென்மை"),
    ("படம்", "திரைப்படம்", "ஓவியம்", "புகைப்படம்"),
    ("பணம்", "காசு", "ரூபாய்", "செல்வம்"),
    ("பணிவு", "அடக்கம்", "எளிமை", "மரியாதை"),
    ("பதவி", "வேலை", "அதிகாரம்", "பொறுப்பு"),
    ("பள்ளி", "கல்வி", "மாணவர்", "ஆசிரியர்"),
    ("பதில்", "கேள்வி", "விடை", "மறுமொழி"),
    ("பரிசு", "அன்பளிப்பு", "வெகுமதி", "போட்டி"),
    ("பறவை", "சிறகு", "கூடு", "வானம்"),
    ("பாடம்", "கல்வி", "ஆசிரியர்", "கற்றல்"),
    ("பாரம்", "எடை", "கனம்", "சுமை"),
    ("பாலம்", "இணைப்பு", "ஆறு", "கடந்துசெல்"),
    ("புகழ்", "பெருமை", "கீர்த்தி", "அவமானம்"),
    ("புதன்", "கோள்", "அறிவன்", "புத்தி"),
    ("புரவி", "குதிரை", "பந்தயம்", "சவாரி"),
    ("பெருமை", "கர்வம்", "புகழ்", "சிறுமை"),
    ("பேச்சு", "வார்த்தை", "மொழி", "உரையாடல்"),
    ("பொழுது", "நேரம்", "காலை", "மாலை"),
    ("பொறுமை", "சகிப்புத்தன்மை", "அவசரம்", "அமைதி"),
    ("போட்டி", "பந்தயம்", "விளையாட்டு", "ஜெயித்தல்"),
    ("மதில்", "சுவர்", "கோட்டை", "பாதுகாப்பு"),
    ("மலர்", "பூ", "செடி", "மணம்"),
    ("மலிவு", "விலை", "குறைவு", "அதிகம்"),
    ("மணல்", "கடற்கரை", "வீடு", "பாலைவனம்"),
    ("மாளிகை", "அரண்மனை", "வீடு", "பெரிய"),
    ("மூட்டு", "இணைப்பு", "முழங்கால்", "முழங்கை"),
    ("மூலிகை", "செடி", "மருந்து", "வேர்"),
    ("வண்டி", "வாகனம்", "சக்கரம்", "பயணம்"),
    ("வண்டு", "பூச்சி", "தேனீ", "ரீங்காரம்"),
    ("வறுமை", "ஏழ்மை", "செல்வம்", "பசி"),
    ("வாடகை", "குடியிருப்பு", "பணம்", "ஒப்பந்தம்"),
    ("வாரம்", "கிழமை", "மாதம்", "ஏழு"),
    ("வாய்மை", "உண்மை", "பொய்", "சத்தியம்"),
    ("வானம்", "ஆகாயம்", "மேகம்", "நீலம்"),
    ("விரல்", "கை", "கால்", "நகம்"),
    ("வெண்மை", "கருமை", "நிறம்", "தூய்மை"),
    ("வெள்ளி", "உலோகம்", "கிழமை", "பளபளப்பு"),
    ("வெற்றி", "தோல்வி", "சாதனை", "மகிழ்ச்சி"),
    ("வேங்கை", "புலி", "விலங்கு", "காடு"),
    ("வேடன்", "வேட்டை", "காடு", "விலங்கு"),
    ("வைகாசி", "மாதம்", "தமிழ்", "இரண்டாம்"),
]
four_letter_words = [
    ("அங்காடி", "கடை", "சந்தை", "வணிகம்"),
    ("அச்சம்", "பயம்", "தைரியம்", "திகில்"),
    ("அரசன்", "ராஜா", "மன்னன்", "ஆளுநர்"),
    ("அறிஞர்", "புலவர்", "ஞானி", "மேதை"),
    ("அறுவடை", "விவசாயம்", "நெல்", "விளைச்சல்"),
    ("ஆசிரியை", "ஆசிரியர்", "மாணவர்", "பாடம்"),
    ("ஆடவர்", "ஆண்கள்", "பெண்கள்", "மனிதர்"),
    ("ஆதவன்", "சூரியன்", "பகல்", "ஒளி"),
    ("ஆபத்து", "அபாயம்", "பாதுகாப்பு", "எச்சரிக்கை"),
    ("ஆயிரம்", "நூறு", "லட்சம்", "எண்"),
    ("இயற்கை", "செயற்கை", "காடு", "செடி"),
    ("இளைஞர்", "வாலிபர்", "முதியவர்", "இளமை"),
    ("உலகம்", "பூமி", "நாடு", "மக்கள்"),
    ("உலோகம்", "தங்கம்", "இரும்பு", "வெள்ளி"),
    ("ஊதியம்", "சம்பளம்", "வருமானம்", "வேலை"),
    ("ஊறுகாய்", "புளிப்பு", "உணவு", "சுவை"),
    ("எண்ணம்", "சிந்தனை", "கருத்து", "நினைவு"),
    ("எரிமலை", "நெருப்பு", "சீற்றம்", "குழம்பு"),
    ("ஏராளம்", "அதிகம்", "நிறைய", "குறைவு"),
    ("ஐப்பசி", "மாதம்", "தமிழ்", "ஏழாம்"),
    ("ஓவியம்", "சித்திரம்", "வரைதல்", "கலை"),
    ("கட்டளை", "ஆணை", "உத்தரவு", "அதிகாரம்"),
    ("கட்டுரை", "எழுத்து", "பத்தி", "வாக்கியம்"),
    ("கண்ணீர்", "அழுகை", "சோகம்", "துளி"),
    ("கணிதம்", "கணக்கு", "எண்", "கூட்டல்"),
    ("கல்லணை", "அணை", "ஆறு", "நீர்"),
    ("கல்லூரி", "படிப்பு", "மாணவர்", "பட்டம்"),
    ("களிமண்", "மண்", "பானை", "சிற்பம்"),
    ("கற்பனை", "நிஜம்", "கனவு", "சிந்தனை"),
    ("கவிஞர்", "புலவர்", "பாட்டு", "இலக்கியம்"),
    ("காய்கறி", "செடி", "உணவு", "சமையல்"),
    ("காரியம்", "செயல்", "வேலை", "நோக்கம்"),
    ("கால்நடை", "மாடு", "ஆடு", "விலங்கு"),
    ("கிராமம்", "ஊர்", "நகரம்", "மக்கள்"),
    ("கூட்டம்", "நெரிசல்", "மக்கள்", "தனிமை"),
    ("கூட்டல்", "கழித்தல்", "கணிதம்", "எண்"),
    ("கூந்தல்", "முடி", "தலை", "அழகு"),
    ("கொண்டாடு", "விழா", "மகிழ்ச்சி", "கொண்டாட்டம்"),
    ("கோபுரம்", "கோயில்", "உயரம்", "வாசல்"),
    ("கோரிக்கை", "வேண்டுகோள்", "விண்ணப்பம்", "மனு"),
    ("சட்டம்", "விதி", "ஒழுங்கு", "நீதி"),
    ("சகோதரி", "அக்கா", "தங்கை", "உடன்பிறப்பு"),
    ("சமூகம்", "மக்கள்", "சமுதாயம்", "நாகரிகம்"),
    ("சித்திரை", "மாதம்", "தமிழ்", "முதல்"),
    ("சிரமம்", "கடினம்", "எளிது", "கஷ்டம்"),
    ("சிற்பம்", "சிலை", "கலை", "அழகு"),
    ("சிறப்பு", "பொது", "முக்கியத்துவம்", "தனித்துவம்"),
    ("சுற்றுலா", "பயணம்", "பிரயாணம்", "சுற்றிப்பார்"),
    ("சூழ்நிலை", "நிலைமை", "சூழல்", "சந்தர்ப்பம்"),
    ("செயற்கை", "இயற்கை", "மனிதனால்", "உருவாக்கப்பட்ட"),
    ("செல்வம்", "வளம்", "பணம்", "சொத்து"),
    ("செவ்வாய்", "கோள்", "கிரகம்", "சிவப்பு"),
    ("தண்டனை", "அபராதம்", "குற்றம்", "சிறை"),
    ("தண்ணீர்", "நீர்", "பருகு", "அத்தியாவசியம்"),
    ("தலைவர்", "வழிகாட்டி", "தலைமை", "நிர்வாகி"),
    ("திங்கள்", "கிழமை", "சந்திரன்", "சோமవారం"),
    ("திருவிழா", "கொண்டாட்டம்", "பண்டிகை", "கூட்டம்"),
    ("தெய்வம்", "கடவுள்", "இறைவன்", "சக்தி"),
    ("தேர்தல்", "வாக்கு", "ஜனநாயகம்", "பிரதிநிதி"),
    ("தொண்ணூறு", "எண்", "நூறு", "பத்தொன்பது"),
    ("பங்குனி", "மாதம்", "தமிழ்", "கடைசி"),
    ("நகரம்", "மாநகரம்", "பட்டணம்", "கிராமம்"),
    ("நடனம்", "ஆட்டம்", "இசை", "கலை"),
    ("நரகம்", "சொர்க்கம்", "பாவம்", "தண்டனை"),
    ("நாடகம்", "நடிப்பு", "மேடை", "கதை"),
    ("நாணயம்", "காசு", "நேர்மை", "உலோகம்"),
    ("நெருப்பு", "தீ", "சூடு", "எரி"),
    ("நூலகம்", "புத்தகம்", "வாசிப்பு", "அறிவு"),
    ("பண்பாடு", "கலாச்சாரம்", "நாகரிகம்", "பாரம்பரியம்"),
    ("பயணம்", "பிரயாணம்", "செலவு", "அனுபவம்"),
    ("பயிற்சி", "பழக்கம்", "கற்றல்", "திறமை"),
    ("பாடகர்", "இசை", "பாட்டு", "குரல்"),
    ("பாராட்டு", "வாழ்த்து", "மரியாதை", "புகழ்ச்சி"),
    ("புன்னகை", "சிரிப்பு", "மகிழ்ச்சி", "முகம்"),
    ("பொங்கல்", "பண்டிகை", "அறுவடை", "சூரியன்"),
    ("பொறுப்பு", "கடமை", "அக்கறை", "பதில்"),
    ("மகளிர்", "பெண்கள்", "தாய்", "சகோதரி"),
    ("மகுடம்", "கிரீடம்", "அரசன்", "அதிகாரம்"),
    ("மஞ்சள்", "நிறம்", "மங்கலம்", "கிழங்கு"),
    ("மந்திரி", "அமைச்சர்", "அரசு", "ஆலோசனை"),
    ("மரியாதை", "மதிப்பு", "வணக்கம்", "பண்பு"),
    ("மல்லிகை", "பூ", "மணம்", "வெண்மை"),
    ("மன்னன்", "அரசன்", "ராஜா", "ஆட்சி"),
    ("மாநிலம்", "தேசம்", "அரசு", "நிர்வாகம்"),
    ("மார்கழி", "மாதம்", "தமிழ்", "ஒன்பதாம்"),
    ("மிருகம்", "விலங்கு", "காடு", "பிராணி"),
    ("மூங்கில்", "மரம்", "புல்", "குழாய்"),
    ("யுத்தம்", "போர்", "சண்டை", "அமைதி"),
    ("வகுப்பு", "பாடம்", "மாணவர்", "அறை"),
    ("வண்ணம்", "நிறம்", "சாயல்", "அழகு"),
    ("வரலாறு", "சரித்திரம்", "கடந்தகாலம்", "நிகழ்வு"),
    ("வருடம்", "ஆண்டு", "மாதம்", "நாள்"),
    ("விஞ்ஞானி", "அறிவியல்", "கண்டுபிடிப்பு", "ஆராய்ச்சி"),
    ("விமானம்", "வானூர்தி", "பற", "ஆகாயம்"),
    ("வியப்பு", "ஆச்சரியம்", "அதிசயம்", "திகைப்பு"),
    ("வியாழன்", "கோள்", "குரு", "கிழமை"),
    ("விளக்கு", "ஒளி", "தீபம்", "வெளிச்சம்"),
    ("விவசாயி", "உழவன்", "நிலம்", "பயிர்"),
    ("வேளாண்மை", "விவசாயம்", "பயிரிடுதல்", "பொருளாதாரம்"),
]
five_letter_words = [
    ("அடிப்படை", "ஆதாரம்", "மூலம்", "தொடக்கம்"),
    ("அடையாளம்", "சான்று", "குறி", "தனித்துவம்"),
    ("அச்சகம்", "அச்சு", "புத்தகம்", "இயந்திரம்"),
    ("அதிகாரம்", "ஆட்சி", "உரிமை", "சக்தி"),
    ("அதிசயம்", "ஆச்சரியம்", "வியப்பு", "அற்புதம்"),
    ("அதிர்ச்சி", "திகைப்பு", "நடுக்கம்", "எதிர்பாராத"),
    ("அமைச்சர்", "மந்திரி", "அரசு", "துறை"),
    ("அரசியல்", "அரசாங்கம்", "கொள்கை", "கட்சி"),
    ("அரண்மனை", "மாளிகை", "ராஜா", "ராணி"),
    ("அறிவிப்பு", "செய்தி", "தகவல்", "விளம்பரம்"),
    ("அறிவியல்", "விஞ்ஞானம்", "ஆராய்ச்சி", "அறிவு"),
    ("அனுபவம்", "பட்டறிவு", "உணர்வு", "நிகழ்வு"),
    ("அவசரம்", "விரைவு", "தாமதம்", "முக்கியம்"),
    ("அவமானம்", "இழிவு", "மரியாதை", "பழி"),
    ("ஆண்டவன்", "கடவுள்", "இறைவன்", "தெய்வம்"),
    ("ஆத்திரம்", "கோபம்", "சினம்", "வெறுப்பு"),
    ("ஆராய்ச்சி", "ஆய்வு", "தேடல்", "கண்டுபிடிப்பு"),
    ("ஆலமரம்", "மரம்", "விழுது", "பறவைகள்"),
    ("இயக்கம்", "அசைவு", "செயல்பாடு", "குழு"),
    ("உதாரணம்", "எடுத்துக்காட்டு", "மாதிரி", "விளக்கம்"),
    ("உரையாடல்", "பேச்சு", "சம்பாஷணை", "கலந்துரையாடல்"),
    ("உறக்கம்", "தூக்கம்", "ஓய்வு", "கனவு"),
    ("உறுதிமொழி", "சத்தியம்", "வாக்குறுதி", "சபதம்"),
    ("ஏற்றுமதி", "இறக்குமதி", "வணிகம்", "வெளிநாடு"),
    ("ஔவையார்", "புலவர்", "கவிஞர்", "மூதாட்டி"),
    ("கடற்கரை", "ஓரம்", "மணல்", "அலை"),
    ("கடிகாரம்", "நேரம்", "மணி", "நொடி"),
    ("கதாநாயகி", "நடிகை", "திரைப்படம்", "முக்கிய பாத்திரம்"),
    ("கதிரவன்", "சூரியன்", "பகல்", "ஒளி"),
    ("கம்பளம்", "விரிப்பு", "தரை", "மென்மை"),
    ("கரிகாலன்", "சோழன்", "மன்னன்", "கல்லணை"),
    ("கல்வெட்டு", "பாறை", "எழுத்து", "சரித்திரம்"),
    ("கற்கண்டு", "சர்க்கரை", "இனிப்பு", "வெள்ளை"),
    ("காட்டுத்தீ", "நெருப்பு", "காடு", "பரவுதல்"),
    ("காப்பியம்", "இலக்கியம்", "கதை", "புராணம்"),
    ("கார்த்திகை", "மாதம்", "தமிழ்", "எட்டாம்"),
    ("குற்றவாளி", "குற்றம்", "நிரபராதி", "தண்டனை"),
    ("கைப்பற்று", "பிடி", "ஆக்கிரமி", "வெற்றி"),
    ("கைவிலங்கு", "சங்கிலி", "கட்டு", "சிறை"),
    ("சகோதரன்", "அண்ணன்", "தம்பி", "உடன்பிறப்பு"),
    ("சங்கீதம்", "இசை", "பாட்டு", "ராகம்"),
    ("சம்பளம்", "ஊதியம்", "வருமானம்", "வேலை"),
    ("சமாதானம்", "அமைதி", "போர்", "ஒப்பந்தம்"),
    ("சிநேகிதன்", "நண்பன்", "தோழன்", "நட்பு"),
    ("சித்திரம்", "ஓவியம்", "வரைபடம்", "கலை"),
    ("சுகாதாரம்", "ஆரோக்கியம்", "தூய்மை", "நல்வாழ்வு"),
    ("செல்வாக்கு", "ஆதிக்கம்", "மதிப்பு", "சக்தி"),
    ("சொர்க்கம்", "மோட்சம்", "நரகம்", "இன்பம்"),
    ("தஞ்சாவூர்", "சோழநாடு", "கோயில்", "ஓவியம்"),
    ("தமிழகம்", "மாநிலம்", "தென்னிந்தியா", "சென்னை"),
    ("தயாரிப்பு", "உற்பத்தி", "உருவாக்கம்", "பொருள்"),
    ("தன்னலம்", "சுயநலம்", "பொதுநலம்", "அகந்தை"),
    ("திருமணம்", "கல்யாணம்", "மணமக்கள்", "உறவு"),
    ("துறைமுகம்", "கப்பல்", "ஏற்றுமதி", "இறக்குமதி"),
    ("தென்மேற்கு", "திசை", "தெற்கு", "மேற்கு"),
    ("தொழிற்சாலை", "ஆலை", "உற்பத்தி", "இயந்திரம்"),
    ("நங்கூரம்", "கப்பல்", "நிறுத்து", "இரும்பு"),
    ("நம்பிக்கை", "பற்று", "உறுதி", "திண்ணம்"),
    ("நிகழ்ச்சி", "நிகழ்வு", "விழா", "ஏற்பாடு"),
    ("நிபந்தனை", "கட்டுப்பாடு", "விதி", "ஒப்பந்தம்"),
    ("நிரூபணம்", "ஆதாரம்", "சான்று", "மெய்ப்பித்தல்"),
    ("நிறுவனம்", "அமைப்பு", "கம்பெனி", "தொழில்"),
    ("நூற்றாண்டு", "நூறு", "வருடம்", "காலம்"),
    ("பதினொன்று", "எண்", "பத்து", "ஒன்று"),
    ("பரிந்துரை", "சிபாரிசு", "ஆலோசனை", "ஆதரவு"),
    ("பலகாரம்", "தின்பண்டம்", "உணவு", "இனிப்பு"),
    ("பம்பரம்", "விளையாட்டு", "சுற்றுதல்", "கயிறு"),
    ("பரம்பரை", "தலைமுறை", "பாரம்பரியம்", "மூதாதையர்"),
    ("பாரதியார்", "கவிஞர்", "தேசபக்தி", "விடுதலை"),
    ("பிரதமர்", "முதன்மை", "அமைச்சர்", "அரசு"),
    ("பின்விளைவு", "விளைவு", "முடிவு", "பாதிப்பு"),
    ("புத்தகம்", "நூல்", "வாசிப்பு", "அறிவு"),
    ("புத்தாண்டு", "புது வருடம்", "கொண்டாட்டம்", "தொடக்கம்"),
    ("புரட்டாசி", "மாதம்", "தமிழ்", "ஆறாம்"),
    ("போராட்டம்", "சண்டை", "எதிர்ப்பு", "முயற்சி"),
    ("மகிழ்ச்சி", "சந்தோஷம்", "இன்பம்", "துக்கம்"),
    ("மதிப்பெண்", "புள்ளி", "தேர்வு", "தரம்"),
    ("மன்னிப்பு", "பொறுத்தல்", "கருணை", "குற்றம்"),
    ("மழைத்துளி", "நீர்", "மேகம்", "துளி"),
    ("மாவட்டம்", "நிர்வாகம்", "பகுதி", "மாநிலம்"),
    ("மிரட்டல்", "அச்சுறுத்தல்", "பயமுறுத்து", "எச்சரிக்கை"),
    ("மின்சாரம்", "சக்தி", "ஒளி", "கம்பி"),
    ("முக்கியம்", "அவசியம்", "முதன்மை", "தேவை"),
    ("முதியவர்", "வயதானவர்", "இளைஞர்", "அனுபவம்"),
    ("மூலதனம்", "முதலீடு", "பணம்", "தொழில்"),
    ("வகுத்தல்", "பிரித்தல்", "கணிதம்", "எண்"),
    ("வகுப்பறை", "பாடம்", "மாணவர்", "ஆசிரியர்"),
    ("வசந்தம்", "பருவம்", "பூக்கள்", "இளவேனில்"),
    ("வடமேற்கு", "திசை", "வடக்கு", "மேற்கு"),
    ("வணக்கம்", "நமஸ்காரம்", "மரியாதை", "வரவேற்பு"),
    ("வரவேற்பு", "உபசரிப்பு", "வருகை", "விருந்தினர்"),
    ("வல்லரசு", "சக்திவாய்ந்த", "நாடு", "பொருளாதாரம்"),
    ("வள்ளுவர்", "திருக்குறள்", "புலவர்", "தெய்வீகம்"),
    ("வாக்கியம்", "சொல்", "மொழி", "பொருள்"),
    ("வியாபாரம்", "வணிகம்", "தொழில்", "லாபம்"),
    ("விவசாயம்", "வேளாண்மை", "உழவு", "பயிர்"),
    ("விளையாட்டு", "ஆட்டம்", "போட்டி", "பொழுதுபோக்கு"),
    ("வினைச்சொல்", "செயல்", "மொழி", "இலக்கணம்"),
    ("வெண்கலம்", "உலோகம்", "சிலை", "பாத்திரம்"),
]
six_letter_words = [
    ("அடைக்கலம்", "புகலிடம்", "தஞ்சம்", "பாதுகாப்பு"),
    ("அரசாங்கம்", "அரசு", "ஆட்சி", "நிர்வாகம்"),
    ("அரிச்சுவடி", "அகரவரிசை", "எழுத்துக்கள்", "அடிப்படை"),
    ("அலங்காரம்", "ஒப்பனை", "அழகு", "ஜோடனை"),
    ("அலங்கோலம்", "சீர்குலைவு", "ஒழுங்கின்மை", "குழப்பம்"),
    ("அலுவலகம்", "காரியாலயம்", "வேலை", "பணியாளர்"),
    ("இசைத்தட்டு", "பாடல்", "இசை", "பதிவு"),
    ("இடியாப்பம்", "உணவு", "அரிசி", "சேவை"),
    ("இயக்குனர்", "நெறியாளர்", "திரைப்படம்", "வழிகாட்டி"),
    ("இலக்கணம்", "மொழி", "விதி", "சொல்"),
    ("இலக்கியம்", "நூல்", "கவிதை", "உரைநடை"),
    ("இறக்குமதி", "ஏற்றுமதி", "வணிகம்", "பொருள்கள்"),
    ("உயிரெழுத்து", "மெய்யெழுத்து", "அகரம்", "உயிர்"),
    ("உலகப்போர்", "சண்டை", "நாடுகள்", "அழிவு"),
    ("உறுப்பினர்", "அங்கத்தினர்", "குழு", "சங்கம்"),
    ("எதிர்காலம்", "வருங்காலம்", "இறந்தகாலம்", "நிகழ்காலம்"),
    ("எழுத்தாளர்", "ஆசிரியர்", "நூல்", "படைப்பாளி"),
    ("ஒத்துழைப்பு", "கூட்டுறவு", "உதவி", "ஒன்றிணைந்து"),
    ("ஒப்புக்கொள்", "சம்மதி", "ஏற்றுக்கொள்", "மறுக்காதே"),
    ("ஒப்பந்தம்", "உடன்படிக்கை", "உடன்பாடு", "கையெழுத்து"),
    ("ஒருமைப்பாடு", "ஒற்றுமை", "வேற்றுமை", "கூட்டு"),
    ("கட்டுப்பாடு", "அடக்கம்", "ஒழுங்கு", "வரம்பு"),
    ("கதாநாயகன்", "நடிகர்", "திரைப்படம்", "முக்கிய பாத்திரம்"),
    ("கரகாட்டம்", "நடனம்", "நாட்டுப்புறம்", "செம்பு"),
    ("கரும்பலகை", "எழுதுபலகை", "பள்ளி", "ஆசிரியர்"),
    ("களஞ்சியம்", "சேமிப்பு", "கிடங்கு", "தானியம்"),
    ("கறிவேப்பிலை", "இலை", "மணம்", "சமையல்"),
    ("கன்யாகுமரி", "முக்கடல்", "தெற்கு", "முனை"),
    ("கிருமிநாசினி", "மருந்து", "அழி", "நுண்ணுயிர்"),
    ("குக்கிராமம்", "சிறிய", "ஊர்", "மக்கள்"),
    ("குடியேறுதல்", "குடிபெயர்தல்", "வசித்தல்", "புதிய இடம்"),
    ("குளிர்காலம்", "பனிக்காலம்", "வேனிற்காலம்", "குளிர்"),
    ("கொண்டாட்டம்", "விழா", "மகிழ்ச்சி", "கொண்டாடு"),
    ("சதவிகிதம்", "நூறு", "பங்கு", "கணக்கு"),
    ("சதுரங்கம்", "விளையாட்டு", "ராஜா", "ராணி"),
    ("சமுத்திரம்", "கடல்", "பெருங்கடல்", "ஆழம்"),
    ("சரித்திரம்", "வரலாறு", "கடந்தகாலம்", "நிகழ்வு"),
    ("சாயங்காலம்", "மாலை", "பொழுது", "இரவு"),
    ("சுதந்திரம்", "விடுதலை", "அடிமைத்தனம்", "உரிமை"),
    ("சுற்றுலாமையம்", "இடம்", "பயணம்", "தகவல்"),
    ("சுறுசுறுப்பு", "ஊக்கம்", "சோம்பல்", "வேகம்"),
    ("சூரியகாந்தி", "பூ", "சூரியன்", "எண்ணெய்"),
    ("செம்மறியாடு", "ஆடு", "விலங்கு", "உரோமம்"),
    ("செல்வந்தர்", "பணக்காரர்", "ஏழை", "செல்வம்"),
    ("தலைநகரம்", "முக்கிய", "நகரம்", "நிர்வாகம்"),
    ("திருக்குறள்", "வள்ளுவர்", "அறம்", "நூல்"),
    ("திருப்புமுனை", "மாற்றம்", "முக்கிய", "நிகழ்வு"),
    ("திருநெல்வேலி", "நகரம்", "அல்வா", "தாமிரபரணி"),
    ("திமிங்கலம்", "மீன்", "கடல்", "பெரியது"),
    ("தீபகற்பம்", "நிலம்", "நீர்", "மூன்று பக்கம்"),
    ("தென்கிழக்கு", "திசை", "தெற்கு", "கிழக்கு"),
    ("தென்னிந்தியா", "மாநிலங்கள்", "கலாச்சாரம்", "உணவு"),
    ("தென்னைமரம்", "மரம்", "தேங்காய்", "இளநீர்"),
    ("தொள்ளாயிரம்", "எண்", "ஆயிரம்", "நூறு"),
    ("நடவடிக்கை", "செயல்பாடு", "தீர்வு", "முன்னேற்றம்"),
    ("நல்லெண்ணெய்", "எண்ணெய்", "எள்", "சமையல்"),
    ("நிகழ்காலம்", "தற்காலம்", "இறந்தகாலம்", "எதிர்காலம்"),
    ("நிரந்தரம்", "நிலையானது", "தற்காலிகம்", "எப்போதும்"),
    ("நீதிமன்றம்", "நீதி", "சட்டம்", "வழக்கு"),
    ("நீர்ப்பாசனம்", "விவசாயம்", "தண்ணீர்", "கால்வாய்"),
    ("நீர்வீழ்ச்சி", "அருவி", "மலை", "தண்ணீர்"),
    ("நெடுந்தூரம்", "தொலைவு", "அருகில்", "பயணம்"),
    ("பச்சைக்கிளி", "பறவை", "நிறம்", "அழகு"),
    ("பஞ்சாங்கம்", "ஜோதிடம்", "நாள்", "நட்சத்திரம்"),
    ("பஞ்சபூதம்", "நிலம்", "நீர்", "நெருப்பு"),
    ("படையெடுப்பு", "தாக்குதல்", "போர்", "ஆக்கிரமிப்பு"),
    ("பண்டமாற்று", "பரிமாற்றம்", "பொருள்", "வணிகம்"),
    ("பத்தொன்பது", "எண்", "இருபது", "பத்து"),
    ("பரப்பளவு", "விஸ்தீரணம்", "நிலம்", "அளவு"),
    ("பற்றாக்குறை", "குறைபாடு", "அதிகம்", "தேவை"),
    ("பல்லாங்குழி", "விளையாட்டு", "குழி", "சோழி"),
    ("பல்லாயிரம்", "பல", "ஆயிரம்", "எண்ணிக்கை"),
    ("பன்னிரண்டு", "எண்", "பதினொன்று", "பதிமூன்று"),
    ("பிரபஞ்சம்", "அண்டம்", "உலகம்", "நட்சத்திரங்கள்"),
    ("பிரம்மாண்டம்", "பெரிய", "மாபெரும்", "மிகையான"),
    ("புளியமரம்", "மரம்", "பழம்", "புளிப்பு"),
    ("பூந்தோட்டம்", "மலர்கள்", "செடிகள்", "அழகு"),
    ("பெயர்ச்சொல்", "இலக்கணம்", "சொல்", "பெயர்"),
    ("பெருங்காயம்", "மசாலா", "மணம்", "சமையல்"),
    ("பெரும்பான்மை", "அதிகம்", "சிறுபான்மை", "மக்கள்"),
    ("பேராசிரியர்", "ஆசிரியர்", "கல்லூரி", "நிபுணர்"),
    ("பொருளாதாரம்", "நிதி", "வளர்ச்சி", "வர்த்தகம்"),
    ("பொழுதுபோக்கு", "ஓய்வு", "மகிழ்ச்சி", "விளையாட்டு"),
    ("பொற்கொல்லன்", "தங்கம்", "நகை", "வேலை"),
    ("போர்க்களம்", "யுத்தக்களம்", "சண்டை", "வீரம்"),
    ("மக்கள்தொகை", "ஜனத்தொகை", "மக்கள்", "எண்ணிக்கை"),
    ("மருத்துவம்", "வைத்தியம்", "சிகிச்சை", "மருந்து"),
    ("மருத்துவர்", "வைத்தியர்", "சிகிச்சை", "நோயாளி"),
    ("மறுபடியும்", "மீண்டும்", "திரும்ப", "ஒருமுறை"),
    ("மிருதங்கம்", "இசைக்கருவி", "தாளம்", "கச்சேரி"),
    ("மாணவர்கள்", "கல்வி", "பள்ளி", "ஆசிரியர்"),
    ("முன்னேற்றம்", "வளர்ச்சி", "பின்தங்கிய", "மேம்பாடு"),
    ("மெய்யெழுத்து", "உயிரெழுத்து", "எழுத்து", "புள்ளி"),
    ("வடகிழக்கு", "திசை", "வடக்கு", "கிழக்கு"),
    ("வர்த்தகம்", "வணிகம்", "வியாபாரம்", "தொழில்"),
    ("வாழைப்பழம்", "பழம்", "மரம்", "உணவு"),
    ("விடியற்காலை", "அதிகாலை", "காலை", "சூரிய உதயம்"),
    ("விண்ணப்பம்", "கோரிக்கை", "மனு", "படிவம்"),
    ("விருந்தினர்", "அழைப்பாளர்", "உபசரிப்பு", "வருகை"),
]

all_words = [
    ("மூன்றெழுத்து",) + w for w in three_letter_words
] + [
    ("நான்கெழுத்து",) + w for w in four_letter_words
] + [
    ("ஐந்தெழுத்து",) + w for w in five_letter_words
] + [
    ("ஆறெழுத்து",) + w for w in six_letter_words
]

for category, keyword, clue1, clue2, clue3 in all_words:
    data["Category"].append(category)
    data["Keyword"].append(keyword)
    data["Clue 1"].append(clue1)
    data["Clue 2"].append(clue2)
    data["Clue 3"].append(clue3)

df = pd.DataFrame(data)
df.to_csv("tamil_word_game.csv", index=False, encoding='utf-8')

print("CSV file 'tamil_word_game.csv' has been created successfully.")