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
                        <li><a href="band-news">News</a></li>
                        <li><a href="tour">Tour</a></li>
                        <li><a target="_blank" href="https://www.spotify.com">Music</a></li>
                    </ul>
                </div>
            </nav>
        </div>

        <div>&nbsp;</div>

        <div class="container" align="center">
            <div class="col-lg-12">
                <div class="presentation">
                    <h1><b>ADMINISTRATION SYSTEM</b></h1>
                </div>
            </div>
        </div>

        <div class="container-fluid" align="center">
            <div class="col-lg-12">
                @if(isset(Auth::user()->email))
                    <script>window.location="administration";</script>
                @endif

                @if ($message = Session::get('error'))
                    <div class="alert alert-danger alert-block">
                        <button type="button" class="close" data-dismiss="alert">×</button>
                        <strong><p>{{ $message }}</p></strong>
                    </div>
                @endif

                @if (count($errors) > 0)
                    <div class="alert alert-danger">
                        <ul>
                            @foreach($errors->all() as $error)
                                <p>{{ $error }}</p>
                            @endforeach
                        </ul>
                    </div>
                @endif

                <div>&nbsp;</div>

                <form method="post" action="{{ url('/login/check-login') }}">
                    @csrf

                    <input type="email" name="email" placeholder="email"/>
                    <div>&nbsp;</div>
                    <input type="password" name="password" placeholder="password"/>
                    <div>&nbsp;</div>
                    <button type="Submit"><h2>Login</h2></button>
                    <div>&nbsp;</div>
                </form>
            </div>
        </div>
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
