@extends('layouts.mainlayout')

@section('content')

    <header>
        <div class="overlay"></div>
        <video id="dreaming" autoplay="autoplay" muted="muted" loop="loop">
            <source src="{{URL('/data/tours_video.mp4')}}" type="video/mp4">
        </video>

        <div align="center">

            @if(isset(Auth::user()->email))
                <nav class="nav-conainer">
                    <input type="checkbox" id="nav" class="hidden"/>
                    <label for="nav" class="nav-open"><i></i><i></i><i></i></label>
                    <div class="nav-container">
                        <ul>
                            <li><a href="/">Home</a></li>
                            <li><a href="/band-news">News</a></li>
                            <li><a href="/tour">Tour</a></li>
                            <li><a target="_blank" href="https://www.spotify.com">Music</a></li>
                            <li><a href="/administration">Administration board</a></li>
                        </ul>
                    </div>
                </nav>
            @else
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
            @endif
        </div>

        <div class="container" align="center">
            <div class="col-lg-12">
                <div class="presentation">
                    <h1><b>BAND TOUR</b></h1>
                    <div>&nbsp;</div>
                    <h2>Stay tuned to find informations about tours, new songs and others</h2>
                </div>
            </div>
        </div>
    </header>

    <div class="white-background">

        <div class="container-fluid" align="center">
            @foreach ($tours as $tours)
                <div class="boundaries">
                    <div class="col-lg-3">
                        <p><b>{{ $tours->space }}</b></p>
                    </div>
                    <div class="col-lg-3">
                        <p>{{ $tours->time }}</p>
                    </div>
                    <div class="col-lg-3">
                        <p>{{ $tours->location }}</p>
                    </div>
                    <div class="col-lg-3">
                        <a target="_blank" class="white-wrapped-cut" href="{{ $tours->ticket }}">Tickets</a>
                    </div>
                </div>
            @endforeach
        </div>
    </div>
@endsection
