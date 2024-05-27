from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lily!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
db = SQLAlchemy(app)
app.app_context().push()

# Functions
def get_company_names_represents():
    companies_represents = Represents.query.all()
    return [company for company in companies_represents]

def get_company_names_recommends():
    companies_represents = Recommends.query.all()
    return [company for company in companies_represents]

@app.context_processor
def inject_companies_represents():
    companies_represents = get_company_names_represents()
    return dict(companies_represents=companies_represents)

@app.context_processor
def inject_companies_recommends():
    companies_recommends = get_company_names_recommends()
    return dict(companies_recommends=companies_recommends)


# Databases
class Represents(db.Model):
    __tablename__ = 'represents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    link = db.Column(db.String)
    image = db.Column(db.String)
    country = db.Column(db.String)
    image_grid = db.Column(db.String)

    @staticmethod
    def add_represents_company(name, description, link, image, country, image_grid):
        company = Represents(name=name, description=description, link=link, image=image, country=country, image_grid=image_grid)
        db.session.add(company)
        db.session.commit()
        return company

    def __repr__(self):
        return f'{self.name}'


class Recommends(db.Model):
    __tablename__ = 'recommends'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    link = db.Column(db.String)
    image = db.Column(db.String)
    country = db.Column(db.String)
    image_grid = db.Column(db.String)


    @staticmethod
    def add_recommends_company(name, description, link, image, country, image_grid):
        company = Recommends(name=name, description=description, link=link, image=image, country=country, image_grid=image_grid)
        db.session.add(company)
        db.session.commit()
        return company
    
    def __repr__(self):
        return f'{self.name}'



# Routes
# @app.route('/base')
# def base():
#     companies = get_company_names()
#     print(f'This is companies: {companies}')
#     return render_template('base.html', companies=companies)


@app.route('/')
def home():
    selected_company = request.args.get('type')
    company = Recommends.query.filter_by(name=selected_company).first()
    return render_template('home.html', company=company)

@app.route('/rahul')
def rahul():
    return render_template('rahul.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/recommends')
def recommends():
    selected_company = request.args.get('type')
    company = Recommends.query.filter_by(name=selected_company).first()
    return render_template('recommends.html', company=company)

@app.route('/represents')
def represents():
    selected_company = request.args.get('type')
    company = Represents.query.filter_by(name=selected_company).first()
    return render_template('represents.html', company=company)




if __name__ == '__main__':
    db.create_all()

    if Represents.query.filter_by(name='Zahara Tours').first() is None:
        Represents.add_represents_company('Zahara Tours', 'Zahara Tours is the oldest premier Destination Management Company in Oman and specializes in crafting programs incorporating local elements for travel' 
                                          ' enthusiasts. We provide innovative and unique experiences showcasing local Omani culture and discovering various ancient traditions through Arts & Crafts. We are' 
                                          ' passionate about travel and pride ourselves on our product knowledge and the range of services we offer. Zahara has an exclusive in-house panel of knowledgeable' 
                                          ' multilingual guides and our own modern transport fleet and we have just invested in new Toyota Land Cruisers. For VIP clients we now have the ability to arrange' 
                                          ' helicopter transfers from Muscat to Wahiba Sands or Jabal Akhdar. Our experiences include dolphin watching & dhow cruises, coffee with a curator, meeting the ladies' 
                                          ' of Sidab cooperative, dinner or a cooking lesson with a family, picnics in wadis, treks in the mountains, camels, quad bikes, private mobile tented camps in the desert,' 
                                          ' turtle viewing, trips along the old frankincense trail and into the magical Empty Quarter.', 'https://www.zaharatours.com/', 'Oman- Boat.jpg', 'Oman', 'Oman Grid.png')
    
    if Represents.query.filter_by(name='Georgica Travel').first() is None:
        Represents.add_represents_company('Georgica Travel', 'GeorgiCa Travel is an established owner driven "dmc" founded in 1998. We have the very best Tour Leaders in Georgia and use the best available cars' 
                                          ' and coaches. GeorgiaCa is one of the few companies with Public Liability Insurance. We offer combination tours of Georgia, Armenia and Azerbaijan. We have superb' 
                                          ' "special access" to museums, palaces, chateaus and monasteries and can organise a private helicopter trip and picnic in the Caucasus mountains! Some of our specials' 
                                          ' include a wine-tasting visit Chateau Mukhrani, the estate of the Georgian princes, where the gardens were designed by the Versailles designer, a private Concert of' 
                                          ' Traditional Polyphonic Singing; stay in the Kakheti wine country at the Tsinandali Estate with its historic wine cellar; visit the Tbilisi Academy of Arts accompanied' 
                                          ' by an Academician; private lunch at a Georgian home with a cooking class of “khinkali” dumplings; a meeting at one of the think - tanks or with a professors of one of' 
                                          ' the leading universities. (We have arranged such meetings for Oxford, Cambridge and Stanford).', 'https://georgicatravel.ge/', 'Georgia- Monastry.jpg', 'Georgia',
                                          'Georgia Grid.png')
    
    if Represents.query.filter_by(name='Dakkak Jordan').first() is None:
        Represents.add_represents_company('Dakkak Jordan', 'Nothing quite prepared for me the impact this delightful country had on me with its amazing contrasts and ancient history. From the fantastic Roman' 
                                          ' remains at Jerash to the weirdly wonderful Dead Sea; sleepy Madaba with its amazing churches and Byzantine mosaics to Mount Nebo from where Moses viewed the promised' 
                                          ' Land; staggeringly beautiful Petra where my walk up to the Monastery was a highlight; Wadi Rum with its magnificent views, amazing luxury camps, proud nomadic Bedouins' 
                                          ' and the famous Hejaz Railway and memories of Lawrence of Arabia. Dakkak Jordan was established in 1955 and can arrange lots of “specials”: being met in the airport' 
                                          ' before Immigration, amazing personable Tour Directors, luxury cars (Land Cruiser, BMW) with wifi dongles, fantastic rates at the luxury 5* hotels, specialist lecturers' 
                                          ' at Jerash & Petra, hot air ballooning, star gazing in the desert, a ride on the historic Hejaz railway, Petra by night, hiking The Wadi Dana trail and staying at an' 
                                          ' eco-lodge at Feynan.', 'https://www.dakkak.com/', 'Jordan- Petra.jpg', 'Jordan', 'Jordan Grid.png')   
           
    if Represents.query.filter_by(name='Dakkak UAE').first() is None:
        Represents.add_represents_company('Dakkak UAE', 'Dakkak dmc is an established owner driven dmc in Dubai for over 10 years. We have 3rd party liability insurance. Our guides are extremely professional and' 
                                          ' our quality control team ensures we provide exemplary service. Dakkak UAE has a New Online System - you can use this to check rates and book' 
                                          ' https://www.dakkakstore.com/agent-registration. There are more than 1000 Hotels available online.  In addition you get access to all our ground services and rates. We' 
                                          ' offer Free Arrival Transfer for any 5 Nights Stay in Dubai which includes Accommodation OR Free Fast Track Service at Dubai Airport for any 5 Nights Stay in Dubai which' 
                                          ' includes Accommodation. Luxury cars for transfers & sightseeing, Amenities package for Honeymooners, Luxury Hotels that we have very good deals with include the Jumeirah' 
                                          ' Group, One & Only, Mandarin Oriental, Ritz Carlton Royal Atlantis The Palm, Mina Seyahi. Our team is experienced, quick and professional and works with Tour Operators' 
                                          ' from the UK USA & Europe.', 'https://www.dakkakuae.com/', 'UAE- Night Boat.jpg', 'UAE', 'UAE Grid.png')     


    if Recommends.query.filter_by(name='Nomads Tours').first() is None:
        Recommends.add_recommends_company('Nomads Tours', 'Discover Mongolia with Nomads Tours ! Dramatic and inspiring landscapes stretch from the Gobi Desert to the vast steppes at the very heart of Mongolia.' 
                                          ' Ride on horseback in the footsteps of the legendary Genghis Khan and experience the hospitality of the traditional nomadic people of the plains in their colourful gers.' 
                                          ' The Nadaam festival is the focal point for many visits along with the less known but spectacular eagle hunting festival. Nomads Tours can customize trips for your FIT' 
                                          ' clients in any part of this spectacular country or help you plan a group trip and provide excellent local Trip Leaders. We have a great new opportunity to provide charter' 
                                          ' flights for up to 10 clients to various parts of the country. Nomads Tours owns and operates the wonderful Tuul Riverside Lodge http://tuulriverside.com/ and also owns' 
                                          ' the most luxurious mobile tented camp in Mongolia.', 'https://nomadstours.com/', 'Mongolia.jpg', 'Mongolia', 'Mongolia Grid.png')
        
    if Recommends.query.filter_by(name='Cosmos').first() is None:
        Recommends.add_recommends_company('Cosmos', 'Cosmos is an excellent ground operator that provides ground services for Tour Operators and shore excursions for Cruise ships. Cosmos has been operating since' 
                                          ' 1978 and works with well-established international Tour Operators. Cosmos is an owner driven company with its own cars, offices across Egypt and Public Liability Insurance.' 
                                          ' The company employs its own team of Egyptologists ensuring excellent quality with guides and vehicles. Some of the "specials" we arrange are… a visit to one of the' 
                                          ' excavation sites in Sakkara; private visits to sites in Egypt before/after visiting hours; cooking classes and a food tasting experience; sailing on the Nile by private' 
                                          ' ultra-luxury Dahabeya from Luxor to Aswan; a lecture with the head of the High Council of Antiquities; a private dinner at any temple in Luxor or Aswan; a meeting on site' 
                                          ' with the  excavation team working on Thutmose III temple or meet with one of the Chicago House excavation team working in Luxor; private balloon ride;  private dinner at' 
                                          ' the Pyramids…', 'http://www.cosmos.com.eg/', 'Egypt.jpeg', 'Egypt', 'Egypt Grid.png')
        
    if Recommends.query.filter_by(name='Encounters Asia').first() is None:
        Recommends.add_recommends_company('Encounters Asia', 'It gives me great pleasure to highly recommend this innovative dmc, owned and run by the charismatic Amit Sankhala. Amit\'s strengths are in customizing' 
                                          ' exclusive experiences for high end FIT clients across India. In Amit\'s words …… my passion is to explore and organize, from specialized walks in Rajasthan\'s magnificent' 
                                          ' cities, to exploring ancient Varanasi at midnight, setting up luxury camps in the middle of nowhere, spending time with our spiritual guru, or transformational experiences' 
                                          ' at festivals. I will create the perfect experience through the right storytelling, with extraordinary guides. The "Star bed" pictured above at Jamtara Wilderness Camp,' 
                                          ' Pench National Park, is the first of its kind in India, designed by Amit. The company owns jungle lodges in the tiger parks of Pench Kanha and Bandhavgarh and has special' 
                                          ' access to scientists and researchers. Our Snow Leopard trips are hugely popular and we work with the Snow Leopard Conservancy and have generated over US$ 50,000 for' 
                                          ' conservation.', 'https://encountersasia.com/', 'india3.jpg', 'India', 'India Grid.png')

    app.run(debug=True)