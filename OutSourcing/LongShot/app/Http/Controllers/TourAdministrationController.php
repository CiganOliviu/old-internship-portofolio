<?php

namespace App\Http\Controllers;

use App\Models\Tour;
use Illuminate\Http\Request;

class TourAdministrationController extends Controller
{

    public function TourAdministrationView()
    {
        return view('administration/tour_administration');
    }

    public function SaveDataToTourTableViews(Request $request)
    {

        $this->validate($request, [
            'location' => 'required',
            'space' => 'required',
            'ticket' => 'required',
            'time' => 'required',
        ]);

        $TourQuerySave = Tour::updateOrCreate(
            [   'location' => $request->location, 'space' => $request->space,
                'ticket' => $request->ticket, 'time' => $request->time
            ],
            [   'location' => $request->location, 'space' => $request->space,
                'ticket' => $request->ticket, 'time' => $request->time
            ],
        );

        $TourQuerySave->save();

        return view('administration/tour_administration_success');
    }
}
