<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Tour extends Model
{
    protected $TourTable = 'Tours';

    protected $fillable = ['location', 'space', 'ticket', 'time'];
}
