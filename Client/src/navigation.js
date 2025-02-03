


import React, { useState, useEffect } from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import DisplayImag from "./DisplayImag"

function Navigation({loadImg}) {
  const [key, setKey] = useState('home');
  const [imagesl, setImages] = useState([]);
     const beforeRanking=()=>{
    

    //   useEffect(() => {
        fetch('http://127.0.0.1:5000/api/get_search_images') // Assuming your Flask API endpoint is /api/getImages
          .then(response => response.json())
          .then(data => {
            setImages(data);
            setKey("profile")
          })
          .catch(error => {
            console.error('Error fetching images:', error);
          });
    //   }, []);
     
  }
  const afterRanking=()=>{
    
 
    console.log("home calling")
    //   useEffect(() => {
        fetch('http://127.0.0.1:5000/api/get_reranked_images') // Assuming your Flask API endpoint is /api/getImages
          .then(response => response.json())
          .then(data => {
            setImages(data);
            setKey("home")
          })
          .catch(error => {
            console.error('Error fetching images:', error);
          });
    //   }, []);
     
  }
  useEffect(() => {console.log("imagesl: ",imagesl)},[imagesl])
  useEffect(() => { console.log("loadImg: ",loadImg)
  if(loadImg){
    setKey("profile")}},[loadImg])
  

  useEffect(() => { 
    setImages([])
    if(key=="home"){
        console.log("home")
        afterRanking()}
    else if(key=="profile"){
        beforeRanking()
    }},[key])

  return (
    <Tabs
      id="controlled-tab-example"
      activeKey={key}
      onSelect={(k) => setKey(k)}
      className="mb-3"
    >
      <Tab eventKey="home" title="Before Mitigation">
      <DisplayImag  imagesl={imagesl}/>
      </Tab>
      <Tab eventKey="profile" title="After Mitigation">
      <DisplayImag  imagesl={imagesl}/>
      </Tab>
      {/* <Tab eventKey="contact" title="Contact" disabled>
        Tab content for Contact
      </Tab> */}
    </Tabs>
  );
}


// const Navigation=()=>   {
//   return (
//     <Tabs
//       defaultActiveKey="profile"
//       id="uncontrolled-tab-example"
//       className="mb-3"
//     >
//       <Tab eventKey="home" title="Home">
//         Tab content for Home
//       </Tab>
//       <Tab eventKey="profile" title="Profile">
//         Tab content for Profile
//       </Tab>
//       <Tab eventKey="contact" title="Contact" disabled>
//         Tab content for Contact
//       </Tab>
//     </Tabs>
//   );
// }
export default Navigation;