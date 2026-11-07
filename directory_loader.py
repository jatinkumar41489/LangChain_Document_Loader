"""
Directory means : A folder in which more than one pdf or txt or other files exist.

DirectoryLoader(
    path = 'Path of Folder / Directory' , 
    glob = 'Which file you want to load from directory'

)

glob --> A Parameter which tells which type of files you want to load from the directory like pdf , txt , csv and other.

## Glob Pattern — Simple Explanation

| Glob Pattern | What It Loads                              |
| ------------ | ------------------------------------------ |
| `**/*.txt`   | All `.txt` files in all subfolders         |
| `*.pdf`      | All `.pdf` files in the root directory     |
| `data/*.csv` | All `.csv` files inside the `data/` folder |
| `**/*`       | All files of any type in all folders       |

Remember:

- `*` → Matches files or names within a single directory.
- `**` → Enables recursive searching through subfolders.
- `.txt`, `.pdf`, `.csv` → File extensions that specify which file types to match.

Example: `**/*.txt` will find `cricket.txt` in the root directory and `.txt` files inside nested folders too.
"""

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# lazy_load() is used to load and process documents one at a time instead of loading all documents into memory at once.
docs = list(loader.lazy_load())

print(len(docs))

for document in docs:
    print(document.metadata)

