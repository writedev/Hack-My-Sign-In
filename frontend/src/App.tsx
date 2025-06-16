import React, { useState } from "react";
import { Button } from "./components/ui/button";
function App() {
  const [currentPage, setCurrentPage] = useState("");

  if (currentPage === "home") {
    return <Home />;
  } else if (currentPage === "about") {
    return <About />;
  }
  return (
    <div>
      <nav className="flex min-h-svh flex-col items-center justify-center">
        <Button
          className="mb-8"
          onClick={() => setCurrentPage("home")}
        >
          Accueil
        </Button>
        <Button onClick={() => setCurrentPage("about")}>À propos</Button>
      </nav>
    </div>
  );
}

function Home() {
  return <h1>Bienvenue sur la page d'accueil !</h1>;
}

function About() {
  return <h1>À propos de nous</h1>;
}

export default App;
