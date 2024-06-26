import React from "react";
import ReactDOM from "react-dom";
import App from "./components/App";
import "./index.css";
import { createRoot } from 'react-dom/client';

import { createBrowserRouter, RouterProvider } from "react-router-dom"
import routes from "./routes";

const router = createBrowserRouter(routes);

const root = createRoot(document.getElementById('root'));
root.render(
    <RouterProvider router={router} />
);
