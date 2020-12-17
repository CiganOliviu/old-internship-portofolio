@extends('layouts.administrationlayout')

@section('content')

    <div class="parallax-background-tour">
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

        <div class="container" align="center">
            <div class="col-lg-12">
                <div class="presentation">
                    <h1><b>ADMINISTRATION SYSTEM</b></h1>
                    <div>&nbsp;</div>
                    <h3>This is the administration board of longshot official website.</h3>
                </div>
            </div>
        </div>
    </div>

    @if(isset(Auth::user()->email))
        <div class="container">
            <div class="col-lg-12" align="center">
                <div class="content">
                    <h1>Welcome {{ Auth::user()->name }}</h1>
                    <div>&nbsp;</div>
                    <h3>Start by adding a new concert into your tour <a href="/band-news-administration">here</a></h3>
                    <div>&nbsp;</div>
                    <h3>Start by adding news about the band <a href="/tour-administration">here</a></h3>
                </div>
            </div>
        </div>
    @else
        <script>window.location = "login";</script>
    @endif


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

