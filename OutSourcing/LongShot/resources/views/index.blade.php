@extends('layouts.mainlayout')

@section('content')

    <header>
        <div class="overlay"></div>
        <video id="dreaming" autoplay="autoplay" muted="muted" loop="loop">
            <source src="{{URL('/data/dreaming.mp4')}}" type="video/mp4">
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
                    <h1><b>THE LONGSHOT BAND</b></h1>
                    <div>&nbsp;</div>
                    <h3>The Longshot is an American rock band formed in Oakland, California in 2018 by Green Day frontman Billie Joe Armstrong.</h3>
                    <div>&nbsp;</div>
                    <i onclick="EnableUnMute()" class="fas fa-volume-up"></i> <i onclick="EnableMute()" class="fas fa-volume-mute"></i>
                </div>
            </div>
        </div>
    </header>
    <div>&nbsp;</div>

    <div class="container" align="center">
        <div class="col-lg-12">
            <div class="content">
                <h1><b>NEW ALBUM “LOVE IS FOR LOSERS…” OUT NOW</b></h1>
                <div>&nbsp;</div>
                <img class="love_is_for_losers_image" src="{{ asset('data/love_is_for_losers.jpeg') }}" alt="love_is_for_losers">
                <div>&nbsp;</div>
                <a href="#"><h2 class="red-wrapped-cut"><b>Stream / Download</b></h2></a>
            </div>
        </div>
    </div>

    <div>&nbsp;</div>

    <div>&nbsp;</div>

    <div class="container-fluid" align="center">
        <div class="col-lg-12">
            <div class="content">
                <h1>Billie Joe's <b>Project</b></h1>
                <div>&nbsp;</div>
                <img class="love_is_for_losers_image" src="{{ asset('data/billie_joe.jpg') }}" alt="love_is_for_losers">
                <div>&nbsp;</div>
                <p>
                    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
                </p>

                <div>&nbsp;</div>

                <p>
                    The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
                </p>
            </div>
        </div>
    </div>

    <div>&nbsp;</div>

    <div>&nbsp;</div>

    <div class="container-fluid" align="center">
        <div class="col-lg-4">
            <div class="content">
                <img class="love_is_for_losers_image" src="{{ asset('data/devils_kind.jpg') }}" alt="love_is_for_losers">
                <a href="#"><h2 class="red-wrapped">Devil's <b>Kind</b></h2></a>
            </div>
        </div>
        <div class="col-lg-4">
            <div class="content">
                <img class="love_is_for_losers_image" src="{{ asset('data/love_is_for_losers_wallpaper.jpg') }}" alt="love_is_for_losers">
                <a href=""><h2 class="red-wrapped">Turn me <b>Loose</b></h2></a>
            </div>
        </div>
        <div class="col-lg-4">
            <div class="content">
                <img class="love_is_for_losers_image" src="{{ asset('data/songs.jpg') }}" alt="love_is_for_losers">
                <a href="#"><h2 class="red-wrapped">Taxi <b>Driver</b></h2></a>
            </div>
        </div>
    </div>

    <div>&nbsp;</div>

    <div>&nbsp;</div>

    <div class="container" align="center">
        <div class="col-lg-12">
            <div class="embed-responsive embed-responsive-16by9">
                <iframe class="youtube_video" width="1250" height="750" src="https://www.youtube.com/embed/z_jjUM2NK5M" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <div>&nbsp;</div>
            <div class="content">
                <a href=""><h2 class="red-wrapped-cut"><b>Stream / Download</b></h2></a>
            </div>
        </div>
    </div>

    <div>&nbsp;</div>

    <div>&nbsp;</div>
@endsection
