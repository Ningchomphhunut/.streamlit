import streamlit as st
import pickle
with open('Tree_model.pkl', 'rb') as model:
    model_dt = pickle.load(model)


def main():
    st.set_page_config(page_title="Car Purchase Prediction App", page_icon="⚕️", layout="centered",
                       initial_sidebar_state="auto")
    html_temp = """ 
    <div style ="background-color:egg;padding:7px">
    <h1 style ="color:black;text-align:center;">Car trading application development Tailored to car buyers</h1> 
        </div><br/>
         <h5 style ="text-align:center;">แอพพลิเคชันการซื้อขายรถยนต์แบบปรับเหมาะกับผู้ซื้อรถยนต์</h5>
         กรุณากรอกข้อมูลด้านล่างนี้ ให้ครบถ้วน
        """

    html_sidebar = """
        <div style ="background-color:egg;padding:9px"> 
    <style>a:link,a:visited {background-color:#e7f5b0;color:black;padding:10px;text-align:center;text-decoration:none;display:inline-block;width: 100%;text-shadow: 2px 2px 5 px #FF99CC;}
    a:hover,a:active {background-color:#ecdc99;}</style>
        <h1 style ="color:black;text-align:center;">ข้อมูลรถยนต์</h1>
                <p style ="color:black;">เนื้อหาข้อมูลด้านล่างนี้ มาจากเว็บไซต์ของ checkraka.com มีความรู้เกี่ยวกับรถยนต์ ทุกรุ่น ทุกยี่ห้อ ให้ผู้ใช้งานได้ค้นคว้าหาข้อมูลที่ท่านต้องการทราบมาไว้ในที่เดียวแล้วค่ะ</p>
                <p><a href="https://www.checkraka.com/car/  " target="_blank">รถยนต์ใหม่</a></p>
                <p><a href="https://www.checkraka.com/car/article/review" target="_blank">รีวิวรถยนต์</a></p>
                <p><a href="https://www.checkraka.com/motorshow/" target="_blank">งานมอเตอร์โชว์</a></p>
                <p><a href="https://www.checkraka.com/car/promotion/" target="_blank">โปรโมชั่นรถใหม่</a></p>
                <p><a href="https://www.magcarzine.com/car-segment-classify/" target="_blank">หมวดหมู่รถยนต์</a></p>
    
    </div> 
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    st.sidebar.write(html_sidebar, unsafe_allow_html=True)
    Buying = st.selectbox("ช่วงระดับราคาซื้อที่คุณต้องการ", ["สูงมาก", "สูง", "ปานกลาง", "ต่ำ", ])
    if Buying == 'สูงมาก':
        Buying = 1
    elif Buying == 'สูง':
        Buying = 2
    elif Buying == 'ปานกลาง':
        Buying = 3
    elif Buying == 'ต่ำ':
        Buying = 4

    Maint = st.selectbox("ราคาในการซ่อมบำรุงรักษารถ", ["สูงมาก", "สูง", "ปานกลาง", "ต่ำ"])
    if Maint == 'สูงมาก':
        Maint = 1
    elif Maint == 'สูง':
        Maint = 2
    elif Maint == 'ปานกลาง':
        Maint = 3
    elif Maint == 'ต่ำ':
        Maint = 4

    Doors = st.selectbox("จำนวนประตูที่คุณต้องการ", ["มากกว่า5ประตู", "5" , "4" , "3" , "2"])
    if Doors == 'มากกว่า5ประตู':
        Doors = 1
    elif Doors == '5':
        Doors = 2
    elif Doors == '4':
        Doors = 3
    elif Doors == '3':
        Doors = 4
    elif Doors == '2':
        Doors = 5

    Persons = st.selectbox("จำนวนที่นั่งที่คุณต้องการ", ["มากกว่า4ที่นั่ง", "4", "2"])
    if Persons == 'มากกว่า4ที่นั่ง':
        Persons = 1
    elif Persons == '4':
        Persons = 2
    elif Persons == '2':
        Persons = 3

    Lug = st.selectbox("ขนาดของช่องเก็บของที่คุณต้องการ", ["ใหญ่", "กลาง", "ขนาดเล็ก"])
    if Lug == 'ใหญ่':
        Lug = 1
    elif Lug == 'กลาง':
        Lug = 2
    elif Lug == 'ขนาดเล็ก':
        Lug = 3

    Safety = st.selectbox("ความปลอดภัยโดยประมาณของรถ", ["สูง","กลาง" ,"ต่ำ" ])
    if Safety == 'สูง':
        Safety = 1
    elif Safety == 'กลาง':
        Safety = 2
    elif Safety == 'ต่ำ':
        Safety = 3

    if st.button('ทำนายผล'):
        result = prediction(Buying, Maint, Doors, Persons, Lug, Safety)
        if (result == 1):
            st.warning('B-Segment เช่น Honda Civic toyota, Corolla Altis, Masda 3 , Nissan Sylphy ')
        elif (result == 2):
            st.success('D-Segment เช่น Toyota Camry, Honda Accord,Nissan Teana')
        elif (result == 3):
            st.success('C-Segment เช่น Honda City, Honad Jazz , Toyota Viost , Mazda2 ')
        elif (result == 4):
            st.success('Eco Car เช่น Nissan March , Nissan Almera, Mitsubishi Mirage , Toyota Yaris Suzuki Swift')


def prediction(Buying, Maint, Doors, Persons, Lug, Safety):
    predicted_output = model_dt.predict([[Buying, Maint, Doors, Persons, Lug, Safety]])
    return predicted_output



if __name__ == '__main__':
    main()
