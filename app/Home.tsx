'use client';

import { Box,Button, Typography, Dialog, DialogTitle, DialogContent, DialogActions } from '@mui/material';
import { useState, useEffect } from 'react';
import LoadingScreen from './LoadingScreen'; // Import the LoadingScreen component
import { validatePrefabElement } from './services/validation';
import type { ChangeEvent } from 'react';

export const maxDuration = 30;

export default function Home() {
  const [loading, setLoading] = useState<boolean>(true); // Loading state
  const [dialogOpen, setDialogOpen] = useState<boolean>(false);
  const [dialogMessage, setDialogMessage] = useState<string>('');

  useEffect(() => {
    const timer = setTimeout(() => {
      setLoading(false); // Set loading to false after 3 seconds
    }, 3000);

    return () => clearTimeout(timer); // Cleanup the timer on component unmount
  }, []);

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      const reader = new FileReader();

      reader.onload = () => {
        const fileContent = reader.result;
        console.log('Encoded file content:', fileContent);
        // You can now use the encoded file content as needed
      };

      reader.onerror = (error) => {
        console.error('Error reading file:', error);
      };

      reader.readAsDataURL(file); // This will encode the file as a base64 string
    }
  };

  const handleButtonClick = () => {
    document.getElementById('fileInput')?.click();
  };

  const handleValidation = () => {
    const result = validatePrefabElement();
    if (result.success) {
      setDialogMessage(`Validation successful: ${result.data}`);
    } else {
      setDialogMessage(`Validation failed: ${result.error}`);
    }
    setDialogOpen(true);
  };

  const handleCloseDialog = () => {
    setDialogOpen(false);
  };

  if (loading) {
    return <LoadingScreen message={'Parser'}/>; // Display the loading screen if loading is true
  }

  return (
    <Box
      sx={{
        width: '100dvw',
        overflow: 'auto',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: 'white',
        minHeight: '90dvh',
        backgroundImage: 'radial-gradient(lightgray 1px, transparent 1px)',
        backgroundSize: '30px 30px',
      }}
    >
      <Typography variant="overline" sx={{ color:'black', marginBottom:'60px', width:'600px', textAlign:'center', lineHeight:'1.5'}}>Parser is the project created during Open source construction hackathon in Munich.</Typography>

      <input
        id="fileInput"
        type="file"
        accept=".pdf"
        style={{ display: 'none' }}
        onChange={handleFileChange}
      />
      <Button
        variant="contained"
        color="primary"
        sx={{
          backgroundColor: 'black',
          color: 'white',
          borderRadius: '30px',
          mb: 2
        }}
        onClick={handleButtonClick}
      >
        Upload PDF
      </Button>
      <Typography variant="caption" sx={{ color:'black', marginTop:'0px'}}>Uploaded pdf is processed using LLM and matched with the library of MOD componets</Typography>
      <Button
        variant="contained"
        color="primary"
        onClick={handleValidation}
        sx={{
          backgroundColor: 'black',
          color: 'white',
          borderRadius: '30px',
          marginTop:'60px',
          mb: 2  // Add margin bottom of 2 units (16px)
        }}
      >
        Validate
      </Button>

      <Dialog open={dialogOpen} onClose={handleCloseDialog}>
        <DialogTitle sx={{ textAlign: 'center' }}><Typography variant="body1">Result</Typography></DialogTitle>
        <DialogContent sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <Typography sx={{ textAlign: 'center' }}>{dialogMessage}</Typography>
        </DialogContent>
        <DialogActions sx={{ justifyContent: 'center', marginBottom:'10px' }}>
          <Button
            size='small'
            onClick={handleCloseDialog}
            sx={{
              backgroundColor: 'black',
              color: 'white',
              borderRadius: '20px',
              pddingBottom: '20px',
              '&:hover': {
                backgroundColor: 'darkgray',
              },
            }}
          >
            Close
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}
