class Univariate:
    def QuanQual(dataset):
        quan = []
        qual = []
        
        for columnNm in dataset.columns:
            if dataset[columnNm].dtype == 'O':
                qual.append(columnNm)
            else:
                quan.append(columnNm)
        
        return quan, qual