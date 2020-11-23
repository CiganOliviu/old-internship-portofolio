<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Newsletter;

class IndexController extends Controller
{
    public function IndexView()
    {
        return view('index');
    }

    public function SaveDataToNewsletterTableViews(Request $request) {

        $NewsletterQuerySave = Newsletter::updateOrCreate(
            [ 'email' => $request->email ],
            [ 'email' => $request->email ]
        );

        $NewsletterQuerySave->save();

        return view('newsletter_subscribe_success');
    }
}
