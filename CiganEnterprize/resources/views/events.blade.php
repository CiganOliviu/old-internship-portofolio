@extends('layout.header')

@section('content')
<header>
  <div class="nav-container">
    <a href="/" class="logo"><h1>Cigan Enterprize</h1></a>
    <a class="navicon-button">
      <div class="navicon"></div>
    </a>
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li class="active"><a href="/events">Events</a></li>
        <li><a href="/industries">industries</a></li>
        <li><a href="/jobs">Jobs</a></li>
        <li><a href="/sediums">Sediums</a></li>
        <li><a href="/blog">Blog</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>
  </div>
</header>

<section id="banner">
  <div id="outer">
    <div id="hero">
      <h2>It's Not Easy Being Green</h2>
    </div>
  </div>
</section>

<section class="wrapper">
  <div id="quote">
    <blockquote>
      There's not a word yet, for old friends who've just met
    </blockquote>
      <a href="http://en.wikipedia.org/wiki/Jim_Henson">Jim Henson</a>
  </div>

  <hr>
  
  <div class="column">
    <p>Kermit the Frog, arguably Jim Henson's most famous Muppet creation, was the star and host of The Muppet Show, played a significant role on Sesame Street, and served as the logo of The Jim Henson Company. He continues to star in the Muppet movies and makes numerous TV appearances.
    <br><br>Kermit grew up with thousands of siblings, and has talked occasionally about other members of his family. His childhood adventures were chronicled in the 2002 video Kermit's Swamp Years. Kermit also has a nephew named Robin.<br><br>Miss Piggy insists that she and Kermit were married in The Muppets Take Manhattan, and that they're very happy. Kermit disagrees, claiming that it was just a movie and that in real life, they have a "professional relationship" (meaning he thinks they're professionals and she thinks they're in a relationship).</p>
  </div>
  
  <div class="column">
    <img src="http://img3.wikia.nocookie.net/__cb20110806233759/muppet/images/1/19/Wedding.mtm.jpg">
  </div>
      
</section>
@endsection