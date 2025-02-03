import DisplayImag from "./DisplayImag"
import Navigation from "./navigation"
import React, { useState, useEffect } from 'react';
const HomePage =()=> {
// function HomePage() {
    const [loadImg, setloadImg] = useState(false)
    const [formData, setFormData] = useState({
        search_key: '',
        no_of_images: ''
      });
      const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData({
          ...formData,
          [name]: value
        });
      };
const handleSubmit=(event)=>{
    setloadImg(false) 
    event.preventDefault();
    console.log(formData)


const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

const raw = JSON.stringify(formData);

const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};

fetch("http://127.0.0.1:5000/handle_post", requestOptions)
  .then((response) => response.text())
  .then((result) => { 
    setloadImg(true)   
//     setFormData({
//     searchKeyword: '',
//     numberOfImages: ''
//   });
   console.log(result)})
  .catch((error) => console.error(error));
}
    return (<div> <h1>Mitigation of Gender Bias </h1>
    
    <form onSubmit={handleSubmit}>
      <label>
        Search Keyword: 
        <input 
          type="text" 
          name="search_key" 
          value={formData.searchKeyword} 
          onChange={handleChange} 
        />
      </label>
      <br />
      <label>
        No of Images: 
        <input 
          type="text" 
          name="no_of_images" 
          value={formData.numberOfImages} 
          onChange={handleChange} 
        />
      </label>
      <br />
      <input type="submit" value="Submit" />
    </form>
        {/* <DisplayImag></DisplayImag> */}
   <Navigation loadImg={loadImg}></Navigation>
     </div>)
}
export default HomePage;