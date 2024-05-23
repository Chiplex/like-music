from django.db import models

class Songs(models.Model):
    ID_Song = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100, blank=False, default='')
    ID_Artist = models.ForeignKey('Artists', on_delete=models.CASCADE)
    Duration = models.FloatField(blank=False, default=0.0)
    Release_Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name_plural = "Songs"

class Artists(models.Model):
    ID_Artist = models.AutoField(primary_key=True)
    Artist_Name = models.CharField(max_length=100, blank=False, default='')

    def __str__(self):
        return self.Artist_Name

    class Meta:
        verbose_name_plural = "Artists"

class Albums(models.Model):
    ID_Album = models.AutoField(primary_key=True)
    Title_Album = models.CharField(max_length=100, blank=False, default='')
    ID_Artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    Release_Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Title_Album

    class Meta:
        verbose_name_plural = "Albums"

class TempoFeatures(models.Model):
    ID_Song = models.ForeignKey(Songs, on_delete=models.CASCADE)
    Tempo_BPM = models.FloatField(blank=False, default=0.0)

    class Meta:
        verbose_name_plural = "Tempo Features"

class DynamicFeatures(models.Model):
    ID_Song = models.ForeignKey(Songs, on_delete=models.CASCADE)
    Dynamic_Level = models.FloatField(blank=False, default=0.0)

    class Meta:
        verbose_name_plural = "Dynamic Features"

class Keys(models.Model):
    ID_Key = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=100, blank=False, default='')

    def __str__(self):
        return self.Description

    class Meta:
        verbose_name_plural = "Keys"

class KeyFeatures(models.Model):
    ID_Song = models.ForeignKey(Songs, on_delete=models.CASCADE, blank=False, null=False)
    ID_Key = models.ForeignKey(Keys, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Key Features"

class Instruments(models.Model):
    ID_Instrument = models.AutoField(primary_key=True)
    Instrument_Name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.Instrument_Name

class Genres(models.Model):
    ID_Genre = models.AutoField(primary_key=True)
    Genre_Name = models.CharField(max_length=100, blank=False, null=False, default='Unknown')

    def __str__(self):
        return self.Genre_Name

class GenreFeatures(models.Model):
    ID_Song = models.ForeignKey(Songs, on_delete=models.CASCADE, blank=False, null=False)
    ID_Genre = models.ForeignKey(Genres, on_delete=models.CASCADE, blank=False, null=False)

class InstrumentFeatures(models.Model):
    ID_Song = models.ForeignKey(Songs, on_delete=models.CASCADE, blank=False, null=False)
    ID_Instrument = models.ForeignKey(Instruments, on_delete=models.CASCADE, blank=False, null=False)   

class Chords(models.Model):
    ID_Chord = models.AutoField(primary_key=True)
    Description_Chord = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.Description_Chord

class ChordFeatures(models.Model):
    ID_Song = models.ForeignKey(Songs, on_delete=models.CASCADE, blank=False, null=False)
    ID_Chord = models.ForeignKey(Chords, on_delete=models.CASCADE, blank=False, null=False)

class Lyrics(models.Model):
    ID_Lyric = models.AutoField(primary_key=True)
    Description_Lyric = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.Description_Lyric

class Emotions(models.Model):
    ID_Emotion = models.AutoField(primary_key=True)
    Description_Emotion = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.Description_Emotion
    
    class Meta:
        verbose_name_plural = "Emotions"

class EmotionFeatures(models.Model):
    ID_Song = models.ForeignKey(Songs, on_delete=models.CASCADE, blank=False, null=False)
    ID_Emotion = models.ForeignKey(Emotions, on_delete=models.CASCADE, blank=False, null=False)

class LyricFeatures(models.Model):
    ID_Song = models.ForeignKey(Songs, on_delete=models.CASCADE, blank=False, null=False)
    ID_Lyric = models.ForeignKey(Lyrics, on_delete=models.CASCADE, blank=False, null=False)