from flask import Flask,render_template,request
import pandas as pd
import pickle
app=Flask(__name__)
model=pickle.load(open('yeild_model.pkl','rb+'))


loc=['Albania',
 'Algeria',
 'Angola',
 'Argentina',
 'Armenia',
 'Australia',
 'Austria',
 'Azerbaijan',
 'Bahamas',
 'Bahrain',
 'Bangladesh',
 'Belarus',
 'Belgium',
 'Botswana',
 'Brazil',
 'Bulgaria',
 'Burkina Faso',
 'Burundi',
 'Cameroon',
 'Canada',
 'Central African Republic',
 'Chile',
 'Colombia',
 'Croatia',
 'Denmark',
 'Dominican Republic',
 'Ecuador',
 'Egypt',
 'El Salvador',
 'Eritrea',
 'Estonia',
 'Finland',
 'France',
 'Germany',
 'Ghana',
 'Greece',
 'Guatemala',
 'Guinea',
 'Guyana',
 'Haiti',
 'Honduras',
 'Hungary',
 'India',
 'Indonesia',
 'Iraq',
 'Ireland',
 'Italy',
 'Jamaica',
 'Japan',
 'Kazakhstan',
 'Kenya',
 'Latvia',
 'Lebanon',
 'Lesotho',
 'Libya',
 'Lithuania',
 'Madagascar',
 'Malawi',
 'Malaysia',
 'Mali',
 'Mauritania',
 'Mauritius',
 'Mexico',
 'Montenegro',
 'Morocco',
 'Mozambique',
 'Namibia',
 'Nepal',
 'Netherlands',
 'New Zealand',
 'Nicaragua',
 'Niger',
 'Norway',
 'Pakistan',
 'Papua New Guinea',
 'Peru',
 'Poland',
 'Portugal',
 'Qatar',
 'Romania',
 'Rwanda',
 'Saudi Arabia',
 'Senegal',
 'Slovenia',
 'South Africa',
 'Spain',
 'Sri Lanka',
 'Sudan',
 'Suriname',
 'Sweden',
 'Switzerland',
 'Tajikistan',
 'Thailand',
 'Tunisia',
 'Turkey',
 'Uganda',
 'Ukraine',
 'United Kingdom',
 'Uruguay',
 'Zambia',
 'Zimbabwe']
crp=['Maize',
 'Potatoes',
 'Rice, paddy',
 'Sorghum',
 'Soybeans',
 'Wheat',
 'Cassava',
 'Sweet potatoes',
 'Plantains and others',
 'Yams']

@app.route('/',methods=['POST','GET'])
def wine_quality():
    if request.method == "POST":
        area=request.form["location"]
        ac=request.form["crop"]
        ap=request.form["pest"]
        ar=request.form["Avg_rain"]
        at=request.form["Avg_temp"]
        id=loc.index(area)
        id1=crp.index(ac)
        print(area,id)
        print(ac,id1)
        print(ap)
        print(ar)
        print(at)
        try:
            pr=model.predict([[id,id1,int(ap),int(ar),int(at)]])
        except:
            pr=[9856]
        return render_template("index.html",q=loc,q1=crp,val=pr[0])
    return render_template('index.html',q=loc,q1=crp)

if __name__=='__main__':
    app.run(debug=True)