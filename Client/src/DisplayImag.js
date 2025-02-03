import { Gallery } from "react-grid-gallery";
import React, { useState, useEffect } from 'react';

const DisplayImag=({ imagesl })=>  {
  
//     const [imagesl, setImages] = useState([]);

// //   useEffect(() => {
//     fetch('http://127.0.0.1:5000/api/getImages') // Assuming your Flask API endpoint is /api/getImages
//       .then(response => response.json())
//       .then(data => {
//         setImages(data);
//       })
//       .catch(error => {
//         console.error('Error fetching images:', error);
//       });
// //   }, []);
//   useEffect(() => {console.log("imagesl: ",imagesl)},[imagesl])



    return (
        // <img src={`./0.jpg`}  />
        <Gallery images={imagesl} />
    );
  }

  export default DisplayImag;