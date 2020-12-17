<?php

namespace App\Http\Controllers;

use App\Models\BandNews;
use Illuminate\Http\Request;

class BandNewsAdministrationController extends Controller
{

    public function BandNewsAdministrationView()
    {

        return view('administration/band_news_administration');
    }

    public function SaveDataToBandNewsTableViews(Request $request)
    {

        $this->validate($request, [
            'title' => 'required',
            'introduction' => 'required',
            'description' => 'required',
            'image' => 'required',
            'author' => 'required',
        ]);

        $BandNewsQuerySave = BandNews::updateOrCreate(
            [   'title' => $request->title, 'introduction' => $request->introduction, 'description' => $request->description,
                'image' => $request->file('image')->store('band_news_images'),
                'author' => $request->author
            ],
            [   'title' => $request->title, 'introduction' => $request->introduction, 'description' => $request->description,
                'image' => $request->file('image')->store('band_news_images'),
                'author' => $request->author
            ],
        );

        $BandNewsQuerySave->save();

        return view('administration/band_news_administration_success');
    }
}
