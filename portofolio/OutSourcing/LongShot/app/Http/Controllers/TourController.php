<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class TourController extends Controller
{
    public function TourView() {

        $tours = DB::table('tours')->get();

        return view('tour_view', [ 'tours' => $tours]);
    }
}
