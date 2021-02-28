@extends('layouts.mainlayout')

@section('content')


<div class="parallax-background-news">
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

    <div>&nbsp;</div>

    <div class="container" align="center">
        <div class="col-lg-12">
            <div class="presentation">
                <h1><b>BAND NEWS</b></h1>
                <div>&nbsp;</div>
                <h2>Stay tuned to find informations about tours, new songs and others</h2>
            </div>
        </div>
    </div>
</div>

<div class="container" align="center">
    <div class="col-lg-12">
        <div class="content">
            @foreach ($band_news as $band_news)
                <div class="content">
                    <h1><b>{{ $band_news->title }}</b></h1>
                    <div>&nbsp;</div>

                    <img class="love_is_for_losers_image" src="images/{{ $band_news->image }}" alt="love_is_for_losers">

                    <div>&nbsp;</div>
                    <p>
                        {{ $band_news->introduction }}
                    </p>

                    <div>&nbsp;</div>

                    <p>
                        {{ $band_news->description }}
                    </p>

                    <div>&nbsp;</div>

                    <p> {{ $band_news->author }} </p>
                </div>
                <div>&nbsp;</div>
            @endforeach
        </div>
    </div>
</div>

@endsection
