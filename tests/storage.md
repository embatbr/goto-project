#Log file for `tests/storage.py`

This is a log file for tests of module `goto/storage`. A object of type `Storage` is created and it's methods are tested.


##stg = Storage()

[goto_dir] /home/embat/.goto
[labels_path] labels
[stack_path] stack


##stg.add_label('home', '/home/embat')

[goto_dir] /home/embat/.goto
[labels_path] labels
[stack_path] stack
[labels]
home            /home/embat


##stg.add_label('musicas', '/home/embat/dados/lazer/musicas')

[goto_dir] /home/embat/.goto
[labels_path] labels
[stack_path] stack
[labels]
home            /home/embat
musicas         /home/embat/dados/lazer/musicas


##stg.add_label('musicas', '/home/embat/Musics')

The label 'musicas' alredy exist.


##path = stg.get_path('musicas')

musicas         /home/embat/dados/lazer/musicas


##path = stg.get_path('jogos')

The label 'jogos' doesn't exist.


##labels = stg.get_all_labels()

{'home': '/home/embat', 'musicas': '/home/embat/dados/lazer/musicas'}


##stg.save()

[goto_dir] /home/embat/.goto
[labels_path] labels
[stack_path] stack
[labels]
home            /home/embat
musicas         /home/embat/dados/lazer/musicas