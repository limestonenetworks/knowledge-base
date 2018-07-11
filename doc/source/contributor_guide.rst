=================
Contributor Guide
=================

Thank you for taking the time to contribute! The following is a set of
guidelines for contributing to ``limestonenetworks/knowledge-base``.
These guidelines are related to adding new articles or editing
existing articles from KB.



1. Make sure that you have a `github account <https://github.com/join>`_.

2. Fork the `limestonenetworks/knowledge-base <https://github.com/limestonenetworks/knowledge-base>`_ repository on github.

.. image:: /image/fork_2.png

3. Once you have forked the repository, it will become your personal
   repository.

.. image:: /image/fork_3.png

4. Under ``/doc/source/`` you can see different folder(``sections``)
   that we have. Please navigate to the intended section, for example
   I want to add an article to ``operatingsystem_support/linux_support/``
   click on ``create new file``.

.. image:: /image/add_article_4.png

5. Provide the article name with ``.rst`` extension.

.. image:: /image/add_article_5.png

6. You can use online `RST compiler <http://rst.ninjs.org/>`_ to preview
   and edit your article.

.. image:: /image/compiler_6.png

7. Please dont forget to mention the ``.. disqus::`` tag at the bottom
   of the article as shown.

.. image:: /image/disqus_7.png

8. After you are done with writing the article, commit the new file
   at the bottom of the page. You can commit it to a Master branch
   or can create new branch.

.. image:: /image/commit_new_file_8.png

9. New article will show up as added to the folder.

.. image:: /image/file_added_9.png

10. You will also need to edit the ``linux_support.rst`` index file under
    ``operatingsystem_support/`` folder.

.. image:: /image/add_to_list_10.png

11. At this point you are ready to open a Pull Request (PR),
    click on ``New pull request``.

.. image:: /image/pr_1.png

12. Click on the ``Create pull request``.

.. image:: /image/pr_2.png

13. Give a suitable title and hit ``Create pull request``.

.. image:: /image/pr_3.png

14. If everything is correct then you should see ``All checks have passed``.

.. image:: /image/pr_4.png

15. If there are errors then PR will fail mentioning the reason for failure.
    Most of the time error will be related to the formating of the article
    as articles are set for `doc8 <https://pypi.org/project/doc8/>`_
    standard.

16. Administrator of the ``limestonenetworks/knowledge-base`` will review
    it and suggest the changes if needed before merging them.

.. disqus::
