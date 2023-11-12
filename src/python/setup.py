from pathlib import Path
from zensols.pybuild import SetupUtil


su = SetupUtil(
    setup_path=Path(__file__).parent.absolute(),
    name="amr_coref",
    package_names=['amr_coref'],
    # package_data={'': ['*.html', '*.js', '*.css', '*.map', '*.svg']},
    package_data={'': ['*.conf', '*.json', '*.yml']},
    description='A python library / model for creating co-references between AMR graph nodes.',
    user='plandes',
    project='amr_coref',
    author='Brad Jascob',
    author_email='bjascob@msn.com',
    url='https://github.com/bjascob/amr_coref',
    keywords=['tooling'],
    has_entry_points=False,
    # Minimal requirements here.  More extensive list in requirements.txt
    install_requires=['amrlib~=0.7.1'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
).setup()
