import React from "react";
import "../styles/Main.css";

import { Link, Routes, Route, Outlet } from "react-router-dom";
import axios from "axios";

import Category from "./Category.jsx";
import Dish from "./Dish.jsx";

function Main() {
  const [categories, setCategories] = React.useState([]);

  React.useEffect(() => {
    axios({
      method: "get",
      url: "http://localhost:8000/api/v1/categories/",
    })
      .then((response) => {
        setCategories(response.data);
      })
      .catch((e) => {
        console.log(e);
      });
  }, []);

  return (
    <React.Fragment>
      <nav className="categories">
        <div className="doc">
          <Link to={""}>Home</Link>
          <a href="http://localhost:8000/swagger" target="_blank">
            Swagger
          </a>
          <a href="http://localhost:8000/doc" target="_blank">
            Doc
          </a>
        </div>
        {categories.map((cat) => {
          return (
            <Link key={cat.id} to={"categories/" + cat.id}>
              {cat.name}
            </Link>
          );
        })}
      </nav>
      <Routes>
        <Route path="*" element={null} />
        <Route path="categories/:id/*" element={<Category />} />
        <Route path="categories/:id/dishes/:id" element={<Dish />} />
      </Routes>
    </React.Fragment>
  );
}

export default Main;
