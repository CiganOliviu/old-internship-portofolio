<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BandNewsController extends Controller
{

    public function BandNewsView()
    {

        $band_news = DB::table('band_news')->get();

        return view('news_view', [ 'band_news' => $band_news]);
    }
}
