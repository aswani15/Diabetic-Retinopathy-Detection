class APTOSDataset(torch.utils.data.Dataset):
    def __init__(self, csv_file, root_dir, transform=None):
        self.aptos_frame = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform
        
    def __len__(self):
        return len(self.aptos_frame)
    
    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir,
                                self.aptos_frame.iloc[idx, 0])
        image = cv2.imread(img_name + ".png", 0)
        
        diagnosis = self.aptos_frame.iloc[idx, 1]
        diagnosis = np.array([diagnosis])
        
        sample = {'image': image, 'diagnosis': diagnosis}
        
        sample["image"] = cv2.resize(sample["image"], (227, 227))
        clahe = CLAHE(clip_limit=3)
        sample = clahe(sample)
        
        if self.transform:
            sample["image"] = self.transform(sample["image"])
            
        return sample