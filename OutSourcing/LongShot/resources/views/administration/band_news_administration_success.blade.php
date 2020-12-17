@extends('layouts.administrationlayout')

@section('content')

    <div class="parallax-background-news">
        <div align="center">
            <nav class="nav-conainer">
                <input type="checkbox" id="nav" class="hidden"/>
                <label for="nav" class="nav-open"><i></i><i></i><i></i></label>
                <div class="nav-container">
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/administration">Administration board</a></li>
                        <li><a href="/band-news-administration">Add News</a></li>
                        <li><a href="/tour-administration">Add concerts in tour</a></li>
                        <li><a href="/logout">Logout</a></li>
                    </ul>
                </div>
            </nav>
        </div>

        <div>&nbsp;</div>

        @if(isset(Auth::user()->email))
            <div class="container" align="center">
                <div class="col-lg-12">
                    <div class="presentation">
                        <h1><b>YOU JUST CREATED A NEWS</b></h1>
                        <div>&nbsp;</div>
                        <h2>Check the post <a href="band-news/">here</a></h2>
                    </div>
                </div>
            </div>
        @else
            <script>window.location = "login";</script>
        @endif
    </div>



    <div class="container-fluid" id="black-background" align="center">
        <div class="col-lg-12">
            <div class="footer">

                <div class="social-media">
                    <a href=""><i class="fab fa-spotify"></i></a>
                    <a href=""><i class="fab fa-facebook-f"></i></a>
                    <a href=""><i class="fab fa-instagram"></i></a>
                    <a href=""><i class="fab fa-twitter"></i></a>
                    <a href=""><i class="fab fa-youtube"></i></a>
                </div>
                <div>&nbsp;</div>
                <p>&copy; 2020 Longshot and reprise records</p>
            </div>
        </div>
    </div>
@endsection
