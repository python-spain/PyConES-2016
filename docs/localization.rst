Localization
============

Transifex client
----------------

Install the Transifex client::

    $ pip install "transifex-client==0.11b3"

To pull the translations done via the web interface into the project::

    $ tx pull -a  # Pull all
    $ tx pull -l en  # Pull only English language

To push translations done locally::

    $ tx push -s -r --skip  # Push all, skipping empty translations

