// import React, { useState, useEffect } from 'react';
// // import './App.css';

// import axios from 'axios';
// // import SearchHeader from './Components/SearchHeader';
// // import nextId from 'react-id-generator';
// // import { BrowserRouter, Route } from 'react-router-dom';
// // import { Link } from 'react-router-dom';
// // import Recipe from './Components/Recipe';
// // import Footer from './Components/Footer';

// function App() {

// 	const [recipes, setRecipe] = useState([]);


// 	useEffect(() => {
// 		// getRecipes(searchString);
// 		console.log('use effect');GET http://localhost:3000/api/v1/feed/ 404 (Not Found
// 	}, []);
// 	function getRecipes() {
// 		const url = `http://localhost:8000/api/v1/feed/`;
// 		axios
// 			.get(url)
// 			.then((response) => {
// 				setRecipe(response.data.sensor);
// 				console.log(response.data.sensor);
// 			})
// 			.catch(console.error);
// 	}

// 	return (
// 		<div className='App'>
// 		<h1>Welcome</h1>
// 		</div>
// 	);
// }

// export default App;