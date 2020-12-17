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
                        <li><a href="administration">Administration board</a></li>
                        <li><a href="band-news-administration">Add News</a></li>
                        <li><a href="/tour-administration">Add concerts in tour</a></li>
                        <li><a href="logout">Logout</a></li>
                    </ul>
                </div>
            </nav>
        </div>

        <div>&nbsp;</div>

        <div class="container" align="center">
            <div class="col-lg-12">
                <div class="presentation">
                    <h1><b>BAND NEWS TOUR</b></h1>
                    <div>&nbsp;</div>
                    <h3>This is the administration page for TOUR page.</h3>
                </div>
            </div>
        </div>
    </div>


    @if(isset(Auth::user()->email))
        <div class="container-fluid">
            <div class="col-lg-12" align="center">
                <div class="content">
                    <h1>Add concert to the tour band!</h1>

                    <div>&nbsp;</div>

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

                    <form action="tour-data" enctype="multipart/form-data" method="Post">
                        @csrf
                        <input type="text" name="location" placeholder="Location of the event" />

                        <div>&nbsp;</div>

                        <input type="text" name="space" placeholder="Space of the event" />

                        <div>&nbsp;</div>

                        <input type="text" name="ticket" placeholder="Tickets for the event"/>

                        <div>&nbsp;</div>

                        <input type="date" name="time" placeholder="Time of the event" />

                        <div>&nbsp;</div>

                        <button type="Submit"><h2>Subscribe</h2></button>
                    </form>
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
