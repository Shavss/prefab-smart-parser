'use client';

import { Box,Button, Typography } from '@mui/material';
import { useState, useEffect } from 'react';
import LoadingScreen from './LoadingScreen'; // Import the LoadingScreen component


export const maxDuration = 30;

export default function Home() {
  const [loading, setLoading] = useState<boolean>(true); // Loading state

  useEffect(() => {
    const timer = setTimeout(() => {
      setLoading(false); // Set loading to false after 3 seconds
    }, 3000);

    return () => clearTimeout(timer); // Cleanup the timer on component unmount
  }, []);

  if (loading) {
    return <LoadingScreen />; // Display the loading screen if loading is true
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
      <Button
        variant="contained"
        color="primary"
        sx={{
          backgroundColor: 'black',
          color: 'white',
          borderRadius: '30px',
        }}
      >
        Upload PDF
      </Button>
      <Typography variant="caption" sx={{ color:'black', marginTop:'20px'}}>Uploaded pdf is processed using LLM and matched with the library of MOD componets</Typography>
    </Box>
  );
}
