<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Auth\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class AuthenticationController extends Controller
{

    public function LoginView()
    {

        return view('administration/login');
    }

    public function CheckLogin(Request $request)
    {
        $this->validate($request, [
            'email' => 'required|email',
            'password' => 'required|alphaNum|min:3',
        ]);

        $user = User::where('email','=', $request->get('email'))->first();

        if ($user != null) {
            Auth::login($user);

            return redirect('administration');
        }
        else
            return back()->with('error', 'Wrong Login Details');
    }

    public function SuccessLoginView() {

        return view('administration/administration');
    }

    public function LogoutView() {

        Auth::logout();

        return redirect('login');
    }
}
