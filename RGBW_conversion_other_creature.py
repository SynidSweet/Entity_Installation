        //'Ri', 'Gi', and 'Bi' correspond to the Red, Green, and Blue inputs.
        var M = Math.Max(Ri, Math.Max(Gi, Bi)); //The maximum value between R,G, and B.
        int Wo =0; //White output
        int Ro=0; //Red output
        int Go=0; //Green output
        int Bo=0; //Blue output

        int av = 0; //Average between the two minimum values
        int hR = 0; //Red with 100% hue
        int hG = 0; //Green with 100% hue
        int hB = 0; //Blue with 100% hue

        //These 4 lines serve to figure out what the input color is with 100% hue.
        float multiplier = 255.0f / M;
        hR = Convert.ToInt32(Ri * multiplier);
        hG = Convert.ToInt32(Gi * multiplier);
        hB = Convert.ToInt32(Bi * multiplier);

        //Depending on the maximum value, get an average of the least used colors, weighted for their importance in the overall hue.
        //This is the problematic part
        if (M == Ri)
           av = (Bi*hB + Gi*hG) / (hB+hG);
        else if (M == Gi)
            av = (Ri*hR + Bi*hB) / (hR+hB);
        else if (M == Bi)
            av = (Gi*hG + Ri*hR) / (hG+hR);

        //Set the rgbw colors
        Wo = av;
        Bo = Bi - av;
        Ro = Ri - av;
        Go = Gi - av;
        if (Wo < 1) Wo = 0;
        if (Bo < 1) Bo = 0;
        if (Ro < 1) Ro = 0;
        if (Go < 1) Go = 0;
        if (Wo > 255) Wo = 255;
        if (Bo > 255) Bo = 255;
        if (Ro > 255) Ro = 255;
        if (Go > 255) Go = 255;