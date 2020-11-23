@extends('layouts.mainlayout')

@section('content')


    <div class="paralax-background-tour">
        <div align="center">
            <nav class="nav-conainer">
                <input type="checkbox" id="nav" class="hidden"/>
                <label for="nav" class="nav-open"><i></i><i></i><i></i></label>
                <div class="nav-container">
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="band-news">News</a></li>
                        <li><a href="tour">Tour</a></li>
                        <li><a href="#">Music</a></li>
                    </ul>
                </div>
            </nav>
        </div>

        <div>&nbsp;</div>

        <div class="container" align="center">
            <div class="col-lg-12">
                <div class="presentation">
                    <h1><b>BAND TOURS</b></h1>
                    <div>&nbsp;</div>
                    <h2>Stay tuned to find informations about tours, new songs and others</h2>
                </div>
            </div>
        </div>
    </div>

    <div>&nbsp;</div>

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
            <div>&nbsp;</div>
        @endforeach
    </div>
@endsection
